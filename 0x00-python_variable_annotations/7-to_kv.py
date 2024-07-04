#!/usr/bin/env python3
"""type-annotated function to_kv"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        args:
            k: str
            v: int | float
        return: Tuple[str, float]
    """
    return k, v**2
