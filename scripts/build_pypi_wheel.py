#!/usr/bin/env python3
"""Assemble a platform wheel from a prebuilt Shiboken6 extension.

Building the native extension requires Qt, PySide6 and shiboken6-generator.
Those dependencies are prepared by CI (or a developer shell) before this
script runs, so it deliberately does not invoke CMake itself.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]

# Warehouse rejects uploads whose wheel filename carries an unnormalized
# project name, so every dist artifact uses this PEP 503 form (the importable
# package itself stays "ElaWidgetTools").
DIST_NAME = "elawidgettools"

METADATA_TEMPLATE = """Metadata-Version: 2.1
Name: elawidgettools
Version: {version}
Summary: Fluent UI widgets for PySide6 / Qt Widgets
Author: CyberWon
License: MIT
Project-URL: Homepage, https://github.com/CyberWon/PySide6ElaWidgetTools
Project-URL: Bug Tracker, https://github.com/CyberWon/PySide6ElaWidgetTools/issues
Keywords: qt,pyside6,widgets,fluent-ui,gui,desktop
Classifier: Development Status :: 4 - Beta
Classifier: Intended Audience :: Developers
Classifier: License :: OSI Approved :: MIT License
Classifier: Operating System :: MacOS
Classifier: Operating System :: Microsoft :: Windows :: Windows 10
Classifier: Operating System :: Microsoft :: Windows :: Windows 11
Classifier: Programming Language :: Python :: 3
Classifier: Programming Language :: Python :: 3.9
Classifier: Programming Language :: Python :: 3.10
Classifier: Programming Language :: Python :: 3.11
Classifier: Programming Language :: Python :: 3.12
Classifier: Topic :: Software Development :: Libraries :: Python Modules
Classifier: Topic :: Software Development :: User Interfaces
Requires-Python: >=3.9,<3.13
Requires-Dist: PySide6==6.10.3
Description-Content-Type: text/markdown; charset=UTF-8

"""

WHEEL_TEMPLATE = """Wheel-Version: 1.0
Generator: ElaWidgetTools-wheel-builder
Root-Is-Purelib: false
Tag: {tag}
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--extension", required=True, type=Path)
    parser.add_argument("--pyi", default=ROOT / "bindings" / "ElaWidgetTools.pyi", type=Path)
    parser.add_argument("--version", required=True)
    parser.add_argument("--python-tag", required=True)
    parser.add_argument("--abi-tag", required=True)
    parser.add_argument("--platform-tag", required=True)
    parser.add_argument("--extra-file", action="append", default=[], type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("dist"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.extension.is_file():
        raise FileNotFoundError(f"Native extension not found: {args.extension}")
    if not args.pyi.is_file():
        raise FileNotFoundError(f"Type stub not found: {args.pyi}")
    if not args.extension.name.startswith("ElaWidgetTools."):
        raise ValueError(f"Unexpected native extension name: {args.extension.name}")
    for extra_file in args.extra_file:
        if not extra_file.is_file():
            raise FileNotFoundError(f"Extra wheel file not found: {extra_file}")

    readme_path = ROOT / "README.md"
    license_path = ROOT / "LICENSE"
    for path in (readme_path, license_path):
        if not path.is_file():
            raise FileNotFoundError(path)

    staging = Path("wheel-staging")
    output_dir = args.output_dir.resolve()
    shutil.rmtree(staging, ignore_errors=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    package_dir = staging / "ElaWidgetTools"
    package_dir.mkdir(parents=True)
    shutil.copy2(args.extension, staging / args.extension.name)
    for extra_file in args.extra_file:
        shutil.copy2(extra_file, staging / extra_file.name)

    init_source = ROOT / "packaging" / "ElaWidgetTools" / "__init__.py"
    init_text = init_source.read_text(encoding="utf-8")
    (package_dir / "__init__.py").write_text(init_text, encoding="utf-8")

    (package_dir / "__init__.pyi").write_bytes(args.pyi.read_bytes())
    (package_dir / "py.typed").write_text("", encoding="utf-8")

    dist_info = staging / f"{DIST_NAME}-{args.version}.dist-info"
    dist_info.mkdir()
    metadata = METADATA_TEMPLATE.format(version=args.version).encode("utf-8")
    metadata += readme_path.read_bytes()
    (dist_info / "METADATA").write_bytes(metadata)
    (dist_info / "WHEEL").write_text(
        WHEEL_TEMPLATE.format(tag=f"{args.python_tag}-{args.abi_tag}-{args.platform_tag}"),
        encoding="utf-8",
    )
    shutil.copy2(license_path, dist_info / "LICENSE")

    command = [
        sys.executable,
        "-m",
        "wheel",
        "pack",
        str(staging),
        "--dest-dir",
        str(output_dir),
    ]
    try:
        subprocess.run(command, check=True)
    except FileNotFoundError as exc:
        raise SystemExit("The 'wheel' package is required; run pip install wheel") from exc
    finally:
        shutil.rmtree(staging, ignore_errors=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
