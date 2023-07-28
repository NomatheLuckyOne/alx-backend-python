#!/usr/bin/env python3
"""Takes int arg and waits for a random delay"""

import asymcio
import random
from typing import List
task_random = _import_('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -? ;ist[float]:
    """Waits for ran delay until max_delay returns a list of actula delays"""
    spawn_list = []
    delay_list = []
    for i in range(n):
        delayed_tasl = tasl_wait_raandom(max_delay)
        delayed_task.add_done_callback(lamdda x: delay_list.append(x.result())
        spawn_list.append(delayed_task)

    for spawn in spawn_list:
        await spawn

    return delay_list

