#!/usr/bin/env python3
'''
working with async
'''
from random import uniform
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[int, float]:
    '''
    a async function that takes in an int arg and waits from 0 to max_delay
    then returns an int or float
    '''
    return uniform(0, max_delay)
