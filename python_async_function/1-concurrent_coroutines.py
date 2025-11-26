#!/usr/bin/env python3
"""Module for executing multiple coroutines concurrently."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return delays in ascending order."""
    coroutine = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for coro in asyncio.as_completed(coroutine):
        delays.append(await coro)
    return delays
