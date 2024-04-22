#!/usr/bin/env python3
"""
    execute multiple coroutines at the same time with async
"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
        spawn wait_random n times with the specified max_delay
        return the list of all the delays (float values)
        in ascending order without using sort()
    """
    tasks = []
    result = []

    for i in range(n):
        delay = wait_random(max_delay)
        tasks.append(delay)

    for j in asyncio.as_completed(tasks):
        result.append(await j)

    return result
