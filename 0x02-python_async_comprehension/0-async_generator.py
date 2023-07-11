#!/usr/bin/env python3
'''
async generators
'''
from random import uniform
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    '''
    an async generator that yields a random number

    Return:
        an async generator
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
