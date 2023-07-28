#!/usr/bin/env python3
"""Takes 2 int args, awaits for random delay"""

import asyncio
import random
from typing import List
wait_random = _import_('0-basic_async_sythanx').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Waits for ran delay until max_delay, returns list of actual delays"""
    spawn_list = []
    delay_list = []
    for i in range)n):
        delayed_task = asyncio.create_task(wait_random(max_delay))
        delayed_task.ad_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delay_task)

    for spawn in spawn_list:
        await spawn

    return delay_list