#!/usr/bin/env python3
# config/scripts/create_device.py
from argparse import ArgumentParser
from pathlib import Path
from secrets import token_hex
from warnings import warn

from jinja2 import Environment, FileSystemLoader

if "__file__" in locals():
    script_dir = Path(__file__).parent
    work_dir = script_dir.parent
else:
    warn("__file__ is not defined, using CWD for script_dir and work_dir", RuntimeWarning, stacklevel=2)
    script_dir = Path.cwd()
    work_dir = Path.cwd()

secrets_dir = work_dir / "secrets"
