"""Runtime loader for the native ElaWidgetTools Shiboken6 extension."""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import sys
from typing import Any

_package_dir = Path(__file__).resolve().parent
_site_packages = _package_dir.parent
_native_suffix = ".pyd" if os.name == "nt" else ".so"
_candidates = sorted(_site_packages.glob(f"ElaWidgetTools.*{_native_suffix}"))

if len(_candidates) != 1:
    raise ImportError(
        "Expected exactly one native ElaWidgetTools extension next to the "
        f"package, found {_candidates}"
    )

# On Windows, the extension links against DLLs bundled by PySide6 and
# shiboken6. Register those directories before loading the extension.
_dll_dirs: list[Any] = []
if os.name == "nt":
    for dependency in ("PySide6", "shiboken6"):
        directory = _site_packages / dependency
        if directory.is_dir():
            _dll_dirs.append(os.add_dll_directory(str(directory)))

_spec = importlib.util.spec_from_file_location("ElaWidgetTools", _candidates[0])
if _spec is None or _spec.loader is None:
    raise ImportError(f"Unable to load native extension: {_candidates[0]}")

_native = importlib.util.module_from_spec(_spec)
sys.modules.setdefault("ElaWidgetTools._native", _native)
_spec.loader.exec_module(_native)

for _name, _value in vars(_native).items():
    if not _name.startswith("__"):
        globals()[_name] = _value

__all__ = [name for name in vars(_native) if not name.startswith("__")]
