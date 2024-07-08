#!/usr/bin/env python3
"""executing multiple coroutines at the same time"""

from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    :param n: int
    :param max_delay: int
    :return: list of all the delays(float values)
    """
    delay_list = []
    # spawn wait_random n times with the max_delay
    for counter in range(0, n):
        # await the wait_random coroutine and store value
        float_value = await wait_random(max_delay)
        delay_list.append(float_value)
    # return the list of all the delays(float values)
    return delay_list
