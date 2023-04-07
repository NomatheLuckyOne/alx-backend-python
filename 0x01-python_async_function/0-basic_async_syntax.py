#!/usr/bin/env python3


import asyncio
from typing import list


wait_random = _import_('0-basic_async_syntax').wait_random


async def main() -> None:
    results: List[float] = []


    results.append(await wait_random())
    results.append(await wait_random(5))
    results.append(await wait_random(15))


    print(results)
