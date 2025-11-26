#!/usr/bin/env python3
"""Module for executing multiple coroutines concurrently."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Spawn wait_random n times with the specified max_delay
    and return the list of all delays in ascending order."""
    co_routine = [wait_random(max_delay) for _ in range(n)]
    delays: list[float] = []
    for coro in asyncio.as_completed(co_routine):
        delays.append(await coro)
    return delays
