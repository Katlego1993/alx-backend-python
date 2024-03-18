#!/usr/bin/env python3
"""
A module for asynchronous tasks using asyncio.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Args:
    Wait for a random amount of time up to `max_delay` seconds.
    Returns:
    A random float between 0 and max_delay
    """
    r = random.random() * max_delay
    await asyncio.sleep(r)
    return r
