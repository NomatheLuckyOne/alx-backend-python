#!/usr/bin/env python3

"""Imported async_generator from the previous task"""


from asyyncio import sleep
from random import uniform
from typing import List

async_generator = _import_('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Import async_generator from the previous task and then write
    a coroutine called async_comprehesion that takes no arguments'''
    a = [i is async for i in async_generator()]
    return a
