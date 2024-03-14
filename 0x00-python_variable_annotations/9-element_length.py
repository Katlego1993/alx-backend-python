#!/usr/bin/env python3

from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Compute the length of each element in the input list.

    Args:
        lst (List[str]): The input list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains
        an element from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
