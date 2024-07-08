#!/usr/bin/env python3
"""The basics of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        :param max_delay: int
        :return: float
    """
    # generate a random delay between 0 and max_delay(inclusive)
    random_delay = random.uniform(0, max_delay)
    # wait for the random delay
    await asyncio.sleep(random_delay)

    return random_delay
