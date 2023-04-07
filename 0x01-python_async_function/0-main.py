import asyncio
import random 



async def wait_random(max_delay=10):
    delay = random.unuform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
