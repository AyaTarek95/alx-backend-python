#!/usr/bin/env python3
import asyncio
import random
"""
asynchronous coroutine that takes in an integer argument
waits for a random delay
eventually return this number
"""


async def wait_random(max_delay: int = 10) -> float:
    """
        takes a number and return it
        after delay
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
