#!/usr/bin/env python3

from typing import Any, List, Union

def safe_first_element(lst: List[Any]) -> Union[Any, None]:
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
