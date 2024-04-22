#!/usr/bin/env python3
"""
The code is nearly identical to wait_n except task_wait_random is being called.
"""
import typing
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """return a sorted ascending list of delays
    """
    tasks = []
    result = []

    for i in range(n):
        tasks.append(task_wait_random(max_delay))

    for j in asyncio.as_completed(tasks):
        result.append(await j)

    return result
