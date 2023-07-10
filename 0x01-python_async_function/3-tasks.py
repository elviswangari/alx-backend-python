#!/usr/bin/env python3
'''
return a asyncio.Task
'''
import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    '''
    a module to schedule a task
    '''
    task = asyncio.create_task(wait_random(max_delay))

    return task
