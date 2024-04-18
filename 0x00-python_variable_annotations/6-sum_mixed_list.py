#!/usr/bin/env python3
"""complex type - sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum of  list of floats and ints"""
    sum: float = 0.0
    for num in mxd_lst:
        sum += num
    return sum
