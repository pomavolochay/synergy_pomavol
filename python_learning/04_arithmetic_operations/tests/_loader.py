from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType


def load_module(module_filename: str, module_name: str) -> ModuleType:
    base_dir = Path(__file__).resolve().parents[1]
    module_path = base_dir / module_filename

    spec = spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load module from {module_path}")

    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
