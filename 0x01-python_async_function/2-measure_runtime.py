#!/usr/bin/env python3
"""Measuring runtime"""

import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures avg time to execute the wait_n n times

    :param n: number of times to call coroutine wait_n
    :param max_delay: maximum delay for calling wait_random
    :return: total_time / n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time = time.time()
    total_time = stop_time - start_time
    return total_time / n
