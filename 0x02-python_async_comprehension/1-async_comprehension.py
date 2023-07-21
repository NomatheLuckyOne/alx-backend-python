#!/usr/bin/env python3


'''Import async_generatorfrom the previous task and then write a
    coroutine called async_comprehension that takes no arguments.

    The coroutine will collect 10 random numbers using an async
    comprehensingover async_generator, then return 10 random numbers.
'''

from typing import List


async def async_comprehension() -> List[float]:
    '''returns a list of random numbers using async comprehension'''

    async_gen = _import_('0-async_generator').async_generator

    rand_num = [i async for i in async_gen()]

    return rand_num

    if _name_ == '_main_':
        import asyncio

        print(asyncio.run(async_comprehension()))
