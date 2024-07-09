#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator function that Loops 10 times,
    each time asynchronously waiting 1 second,
    then yields a random number between 0 and 10.
    """
    tasks = [asyncio.sleep(1) for _ in range(10)]
    await asyncio.gather(*tasks)
    for _ in range(10):
        yield random.uniform(0, 10)
