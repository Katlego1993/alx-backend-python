#!/usr/bin/env python3

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple where the first element is a string and the second element
    is the square of an int or float.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string key
        and the second element is the square of the integer or float value.
    """
    return k, v ** 2.0 if isinstance(v, (int, float)) else 0.0
