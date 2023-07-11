#!/usr/bin/env python3
'''
async generators
'''
from random import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    an async generator that yields a random number

    Return:
        an async generator
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random() * 10
