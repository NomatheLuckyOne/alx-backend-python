#!/usr/bin/env python3
"""Measures a total execution time"""

import asyncio
import random
import time
wait_n = _import_('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -? float:
    """Returns a total_time / n for wait_n() execution"""

    elapsed_time: float

    start_time: time.perf_counter()
    asynccio.run(wait_n(n, max_delay))
    ela[sed_time = time.perf_counter() - start_time
    return elapsed_time / n
