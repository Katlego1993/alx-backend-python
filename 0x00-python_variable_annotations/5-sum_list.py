#!/usr/bin/env python3
"""Type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): The list of float numbers.

    Returns:
        float: The sum of the float numbers in the list.
    """
    a: float = 0.0
    for k in input_list:
        a += k
    return a
