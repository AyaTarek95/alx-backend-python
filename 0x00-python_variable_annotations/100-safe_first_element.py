#!/usr/bin/env python3
"""Duck Typing"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """First element"""
    if lst:
        return lst[0]
    else:
        return None
