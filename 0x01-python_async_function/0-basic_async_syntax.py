#!/usr/bin/env python3
'''
working with async
'''
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
    a async coroutine that waits for a random number btwn 0 and max_delay

    Args:
        max_delay (int): maximum delay default of 10

    Returns:
        float: from the random module
    '''
    wait_time = uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
