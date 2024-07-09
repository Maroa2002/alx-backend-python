#!/usr/bin/env python3


import asyncio
from typing import AsyncGenerator


async def nums(numbers: int) -> AsyncGenerator[int, None]:
    """
    Asynchronous generator function that yields values from 0 to numbers-1,
    pausing for 0.5 seconds between each yield
    """
    for i in range(numbers):
        yield i
        await asyncio.sleep(0.5)


async def test():
    """
    Uses an asynchronous list comprehension to collect odd numbers from nums
    """
    odd_nums = [i async for i in nums(10) if i % 2]
    return odd_nums

# Return the coroutines and print the result
async_list = asyncio.run(test())
print(async_list)
