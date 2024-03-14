#!/usr/bin/env python3

from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]
                     = None) -> Union[Any, T]:
    """
    Safely get the value associated with the given key from the dictionary.

    Args:
        dct (Dict[K, V]): The input dictionary.
        key (K): The key to search for in the dictionary.
        default (Optional[V], optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        Optional[V]: The value associated with the key if it exists, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
