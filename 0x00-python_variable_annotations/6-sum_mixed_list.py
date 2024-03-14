#!/usr/bin/env python3

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list containing integers and floats.

    Returns:
        float: The sum of the integers and floats in the list.
    """
    return sum(mxd_lst)
