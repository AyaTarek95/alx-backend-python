#!/usr/bin/env python3
"""complex type - element_length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """take Itarable and return  elements with len"""
    return [(i, len(i)) for i in lst]
