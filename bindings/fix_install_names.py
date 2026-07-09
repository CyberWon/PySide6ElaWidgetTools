#!/usr/bin/env python3
"""Post-link fixup for the ElaWidgetTools Python extension on macOS.

The C++ library is compiled against a system Qt (e.g. Homebrew) which ships
its own QtCore/QtGui/QtWidgets. PySide6, however, bundles a *different* build
of the same Qt version under ``site-packages/PySide6/Qt/lib``. If the extension
records absolute paths to the system Qt, dyld ends up loading two conflicting
copies of Qt at runtime (symbol-not-found errors such as
``QEventDispatcherGlib::qt_metacall``).

This script rewrites the just-linked extension so that:

* every ``Qt*.framework`` dependency is referenced as ``@rpath/...`` (the same
  convention PySide6's own modules use), and
* the only rpaths are ``@loader_path/PySide6/Qt/lib``,
  ``@loader_path/PySide6`` and ``@loader_path/shiboken6``.

With those rpaths the extension resolves Qt, libpyside6 and libshiboken6
relative to its own location, so it works as long as it is installed anywhere
inside the Python environment's ``site-packages`` directory (next to the
``PySide6`` and ``shiboken6`` folders).

Usage: fix_install_names.py <path/to/ElaWidgetTools.cpython-*.so>
"""

import os
import re
import subprocess
import sys


QT_FW_RE = re.compile(r"^\s*(.*/(Qt[A-Za-z0-9]+\.framework/Versions/A/Qt[A-Za-z0-9]+))\b")


def run(args):
    return subprocess.check_output(args, text=True)


def otool_l(path):
    return run(["otool", "-L", path]).splitlines()


def rpaths(path):
    out = run(["otool", "-l", path])
    paths = []
    lines = out.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == "cmd LC_RPATH":
            for j in range(i + 1, min(i + 4, len(lines))):
                m = re.search(r"path\s+(.+?)\s+\(offset", lines[j])
                if m:
                    paths.append(m.group(1))
                    break
    return paths


def main():
    if len(sys.argv) != 2:
        print("usage: fix_install_names.py <module.so>", file=sys.stderr)
        return 2
    target = sys.argv[1]
    if not os.path.exists(target):
        print(f"fix_install_names: not found: {target}", file=sys.stderr)
        return 1

    cmd = ["install_name_tool"]
    changes = 0
    for line in otool_l(target):
        m = QT_FW_RE.match(line)
        if m:
            abs_path = m.group(1)
            rel = m.group(2)
            cmd += ["-change", abs_path, f"@rpath/{rel}"]
            changes += 1
    if changes:
        cmd += [target]
        run(cmd)
        print(f"fix_install_names: rewrote {changes} Qt framework reference(s) to @rpath")
    else:
        print("fix_install_names: no Qt framework references to rewrite")

    # Replace rpaths: drop everything, add the three @loader_path entries.
    for rp in rpaths(target):
        run(["install_name_tool", "-delete_rpath", rp, target])

    desired = [
        "@loader_path/PySide6/Qt/lib",
        "@loader_path/PySide6",
        "@loader_path/shiboken6",
    ]
    have = set(rpaths(target))
    for rp in desired:
        if rp not in have:
            run(["install_name_tool", "-add_rpath", rp, target])
    print(f"fix_install_names: rpaths now {rpaths(target)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
