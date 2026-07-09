#!/usr/bin/env python3
"""Post-process shiboken-generated wrapper sources.

Some classes that expose no public constructor (they are meant to be used
through static factory methods, e.g. ElaMessageBar / ElaSnackbar / ElaToast)
trigger a shiboken6 generator bug: the ``%CLASS_NAME`` template variable is
left unsubstituted in the "call base virtual method" dispatch code, producing
invalid C++ such as ``cppSelf->::%CLASS_NAME::paintEvent(...)``.

This script rewrites every ``%CLASS_NAME`` occurrence in a generated
``*_wrapper.cpp`` to the actual wrapped class name, which is reliably
declared in the same file as ``reinterpret_cast< ::ClassName *>(Shiboken::Conversions::cppPointer(...)``.
"""

import os
import re
import sys

_CLASS_NAME_RE = re.compile(
    r"reinterpret_cast<\s*::\s*([A-Za-z_][A-Za-z0-9_]*)\s*\*>\s*\(\s*Shiboken::Conversions::cppPointer"
)


def patch_file(path: str) -> bool:
    with open(path, "r", encoding="utf-8") as fh:
        src = fh.read()
    if "%CLASS_NAME" not in src:
        return False
    m = _CLASS_NAME_RE.search(src)
    if not m:
        print(f"fix_class_name: WARNING no class name found in {path}", file=sys.stderr)
        return False
    class_name = m.group(1)
    patched = src.replace("%CLASS_NAME", class_name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(patched)
    print(f"fix_class_name: patched %CLASS_NAME -> {class_name} in {os.path.basename(path)}")
    return True


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: fix_class_name.py <generated_sources_dir>", file=sys.stderr)
        return 2
    gen_dir = sys.argv[1]
    patched_any = False
    for name in os.listdir(gen_dir):
        if name.endswith("_wrapper.cpp"):
            if patch_file(os.path.join(gen_dir, name)):
                patched_any = True
    return 0


if __name__ == "__main__":
    sys.exit(main())
