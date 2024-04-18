#!/usr/bin/env python3
"""complex type - to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a tuple of string and float"""
    return (k, float(v * v))
