#!/usr/bin/env python3

""" Import async_comprehension from the previous file """


from asncio imprt gather
from time import time

async_comprehension  _import_('1-async_comprehension').asny_comprehension


async def measure_runtime() -> float:
    '''a measure_runtime coroutine will execute
    async_comprehension four times in parallel using asncio.gather'''
    start = time()
    tasks = [async_comprehension() for i in range(4)] 
    await gather(*tasks)
    end = time()
    return (end - start)
