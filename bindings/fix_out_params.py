#!/usr/bin/env python3
"""Make ElaWindow navigation-node constructors return the generated key.

The C++ methods ``ElaWindow::addExpanderNode``, ``addFooterNode`` and
``addCategoryNode`` communicate the newly-created node key back to the caller
through a non-const ``QString&`` out-parameter, e.g.:

    ElaNavigationType::NodeResult addExpanderNode(const QString& title,
                                                   QString& key,
                                                   ElaIconType::IconName = ...);

shiboken6 only auto-promotes an out-reference to a tuple element when the C++
return type is ``void`` (the ``--enable-return-value-heuristic`` flag). Because
these methods return ``ElaNavigationType::NodeResult`` (a non-void enum), the
generated wrapper converts the return value but **discards** the key written
into the ``QString&`` argument — see ``elawindow_wrapper.cpp`` where
``cppArg1`` is passed to the C++ call yet only ``&cppResult`` is copied back.

Consequence in Python: ``addExpanderNode(...)`` returns just the ``NodeResult``
and the generated node key is unreachable, so callers cannot nest pages under
an expander/footer/category (every subsequent ``addPageNode(..., key, ...)`` /
``expandNavigationNode(key)`` has nothing to pass).

This script post-processes ``elawindow_wrapper.cpp`` so each affected overload
returns a 2-tuple ``(NodeResult, key)`` instead of the bare ``NodeResult``.
The key argument stays in the Python signature as an in/out parameter
(callers pass an empty string placeholder and unpack the tuple).

The mapping of (function, overload) -> key argument variable is hard-coded
from the deterministic shiboken output:

    addCategoryNode case 0 -> cppArg1   (title, key&)
    addCategoryNode case 1 -> cppArg1   (title, key&, targetKey)
    addExpanderNode  case 0 -> cppArg1  (title, key&, awesome=)
    addExpanderNode  case 1 -> cppArg1  (title, key&, targetKey, awesome=)
    addFooterNode    case 0 -> cppArg1  (title, key&, keyPoints=, awesome=)
    addFooterNode    case 1 -> cppArg2  (title, page*, key&, keyPoints=, awesome=)
"""

import os
import re
import sys

# (function name, case index, key variable holding the QString& out-param)
TARGETS = [
    ("addCategoryNode", 0, "cppArg1"),
    ("addCategoryNode", 1, "cppArg1"),
    ("addExpanderNode", 0, "cppArg1"),
    ("addExpanderNode", 1, "cppArg1"),
    ("addFooterNode", 0, "cppArg1"),
    ("addFooterNode", 1, "cppArg2"),
]

# The exact line shiboken emits to convert the NodeResult return value.
NODE_RESULT_LINE = (
    "pyResult = Shiboken::Conversions::copyToPython("
    "PepType_SETP(reinterpret_cast<SbkEnumType *>"
    "(Shiboken::Module::get(SbkElaWidgetToolsTypeStructs[SBK_ElaNavigationType_NodeResult_IDX])))->converter, &cppResult);"
)


def build_replacement(key_var: str, indent: str) -> str:
    """C++ block (indented) that returns (NodeResult, key) instead of NodeResult."""
    body = [
        "{",
        "    PyObject *_pyNr = Shiboken::Conversions::copyToPython("
        "PepType_SETP(reinterpret_cast<SbkEnumType *>"
        "(Shiboken::Module::get(SbkElaWidgetToolsTypeStructs[SBK_ElaNavigationType_NodeResult_IDX])))->converter, &cppResult);",
        "    PyObject *_pyKey = Shiboken::Conversions::copyToPython("
        "SbkPySide6_QtCoreTypeConverters[SBK_QString_IDX], &" + key_var + ");",
        "    pyResult = PyTuple_New(2);",
        "    PyTuple_SET_ITEM(pyResult, 0, _pyNr);",
        "    PyTuple_SET_ITEM(pyResult, 1, _pyKey);",
        "}",
    ]
    return "\n".join(indent + line for line in body)


def patch_function(src: str, fn: str, case_idx: int, key_var: str) -> str:
    case_marker = "case %d: // %s(" % (case_idx, fn)
    start = src.find(case_marker)
    if start == -1:
        raise SystemExit("fix_out_params: case marker not found: %r" % case_marker)
    # window ends at the break; that closes this case
    break_idx = src.find("break;", start)
    if break_idx == -1:
        raise SystemExit("fix_out_params: break; not found after %r" % case_marker)
    window = src[start:break_idx]
    occurrences = window.count(NODE_RESULT_LINE)
    if occurrences != 1:
        raise SystemExit(
            "fix_out_params: expected exactly 1 NodeResult line in %s case %d, got %d"
            % (fn, case_idx, occurrences)
        )
    tgt = window.find(NODE_RESULT_LINE)
    # leading whitespace of the target line
    line_start = window.rfind("\n", 0, tgt) + 1
    indent = window[line_start:tgt]
    full_target = indent + NODE_RESULT_LINE
    replacement = build_replacement(key_var, indent)
    new_window = window.replace(full_target, replacement, 1)
    return src[:start] + new_window + src[break_idx:]


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: fix_out_params.py <generated_sources_dir>", file=sys.stderr)
        return 2
    gen_dir = sys.argv[1]
    path = os.path.join(gen_dir, "elawindow_wrapper.cpp")
    if not os.path.exists(path):
        print("fix_out_params: not found: %s" % path, file=sys.stderr)
        return 1
    with open(path, "r", encoding="utf-8") as fh:
        src = fh.read()
    # shiboken 6.10+ 的 wrapper 可能不直接 include Python.h，
    # 但 PyTuple_New / PyTuple_SET_ITEM 需要 Python C API 头文件
    if "#include <Python.h>" not in src:
        src = "#include <Python.h>\n" + src
        print("fix_out_params: injected #include <Python.h> at top of elawindow_wrapper.cpp")
    n = 0
    for fn, case_idx, key_var in TARGETS:
        src = patch_function(src, fn, case_idx, key_var)
        n += 1
        print("fix_out_params: patched %s case %d -> (NodeResult, %s)" % (fn, case_idx, key_var))
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(src)
    print("fix_out_params: patched %d overload(s) in elawindow_wrapper.cpp" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
