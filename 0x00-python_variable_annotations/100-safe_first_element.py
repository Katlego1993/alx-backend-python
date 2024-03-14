#!/usr/bin/env python3
"""Defines duck typed function"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely returns the first element of a list if it exists, otherwise returns None.

    Args:
        lst (List[Any]): The input list of any type.

    Returns:
        Union[Any, None]: The first element of the list if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
