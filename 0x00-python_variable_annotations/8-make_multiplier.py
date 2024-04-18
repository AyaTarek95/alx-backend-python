#!/usr/bin/env python3
"""complex type - make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return function that multiplie  float by multiplier"""
    def func(x: float) -> float:
        return x * multiplier
    return func
