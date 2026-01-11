"""Utility helpers for screen_pause."""

import os
from typing import Any

import numpy as np


def save_as_npz(data: Any, filename: str, data_dir: str = "data") -> str:
    """
    Save data to a compressed .npz file under data_dir.

    Returns the file path written.
    """
    os.makedirs(data_dir, exist_ok=True)
    filepath = os.path.join(data_dir, f"{filename}.npz")
    np.savez_compressed(filepath, data=data)
    return filepath
