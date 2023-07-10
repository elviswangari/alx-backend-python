#!/usr/bin/env python3
'''
module for calling multiple async
'''
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    a coroutine module that returns a list of delays

    Args:
        n: an int to repeesent number of times
        max_delay: maximum delays

    Returns:
        a sorted lists of flaots
    '''
    wait_time = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
        )
    return sorted(wait_time)
