#!/usr/bin/env python3
import asyncio
import random
"""
task0
"""
async def wait_random(max_delay: int = 10) -> float:
    """
    return randomdelay
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)

    return random_delay
