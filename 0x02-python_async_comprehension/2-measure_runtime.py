#!/usr/bin/env python3
'''
measure time
'''
import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    measure exec time
    '''
    time_before = perf_counter()
    await asyncio.gather(async_comprehension())
    return (perf_counter() - time_before)
