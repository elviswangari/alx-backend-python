#!/usr/bin/env python3
'''
measure time module
'''
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    a function to measure time taken to exec

    Args:
        n: an int to specifie how long
        max_delay: an int of delay

    Returns:
        a float of time taken
    '''
    time_before = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - time_before
    return (total_time/n)
