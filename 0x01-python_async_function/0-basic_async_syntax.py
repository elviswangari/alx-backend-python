#!/usr/bin/env python3
'''
working with async
'''
from random import uniform
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    '''
    a async function that takes in an int arg and waits from 0 to max_delay
    then returns an int or float
    '''
    wait_time = uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
