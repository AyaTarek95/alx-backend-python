#!/usr/bin/env python3
import asyncio
import random
"""The basics of async"""


async def wait_random(max_delay: int = 10) -> float:
    """awaits for random delay and return it"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)

    return random_delay
