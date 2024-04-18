#!/usr/bin/env python3
"""complex type - sum list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return  sum of  list of floats"""
    sum: float = 0.0
    for num in input_list:
        sum += num
    return sum
