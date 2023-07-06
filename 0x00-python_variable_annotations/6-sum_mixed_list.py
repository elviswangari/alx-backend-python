#!/usr/bin/env python3
'''
module for returning floats
'''
from typing import Union


def sum_mixed_list(mxd_lst:Union[int, float]) -> float:
    '''
    takes in mixed list sums and returns float
    '''
    return float(sum(mxd_lst))
