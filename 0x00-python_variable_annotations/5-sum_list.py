#!/usr/bin/env python3
"""type-annotated function sum_list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        args:
            input_list: List[float]
        return: float
    """
    return sum(input_list)
