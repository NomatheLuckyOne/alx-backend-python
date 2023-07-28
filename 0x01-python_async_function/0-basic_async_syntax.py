#!/usr/bin/env python3
"""Afunction that takes int arg, waits for random delay"""

import asyncio
importrandom


async def wait(max_delay: int = 10) -> float:
    """waits for the delay"""
    actual_delay: float = random.uniform(0, max_delay)
    await asynccio.sleep(actual_delay)
    return actul_delay
