#!/usr/bin/env python3
# config/scripts/create_device.py
from pathlib import Path
from warnings import warn

if "__file__" in locals():
    script_dir = Path(__file__).parent
    work_dir = script_dir.parent
else:
    warn("__file__ is not defined, using CWD for script_dir and work_dir", RuntimeWarning)
    script_dir = Path.cwd()
    work_dir = Path.cwd()

secrets_dir = work_dir / "secrets"
