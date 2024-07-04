#!/usr/bin/env python3
"""type-annotated function sum_mixed_list"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
        args:
            input_list: List[Union[float, int]]
        return: float
    """
    return sum(mxd_list)
