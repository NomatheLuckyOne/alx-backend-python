#!/usr/bin/env python3

"""imported async_generator from the previous task"""


from asyncio import sleep
from random import uniform
from typing import list

async_generator = _import_('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Import async_generator from the previous
    task and then write a coroutine called async_comprehension
    that takes no arguements '''
    a = {i async for i in async_generator()}
    return a
