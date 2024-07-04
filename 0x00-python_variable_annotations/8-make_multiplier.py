#!/usr/bin/env python3
"""type-annotated function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        args:
            multiplier: float
        return: Callable[[float], float]
    """
    def inner_make_multiplier(x: float) -> float:
        """
        args:
            x: float
        return: float
        """
        return x * multiplier
    return inner_make_multiplier
