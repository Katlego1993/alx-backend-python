#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list containing integers and floats.

    Returns:
        float: The sum of the integers and floats in the list.
    """
    a: float = 0.0
    for k in mxd_lst:
        a += k
    return a
