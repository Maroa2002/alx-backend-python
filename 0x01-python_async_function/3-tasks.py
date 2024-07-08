#!/usr/bin/env python3
"""creating a task"""

import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    creates a task

    :param max_delay: max delay for calling wait_random
    :return: asyncio.Task
    """
    random_task = asyncio.create_task(wait_random(max_delay))
    return random_task
