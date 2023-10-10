#!/usr/bin/env python3
"""
This module defines an async generator coroutine called async_generator.
"""

import asyncio
import random

async def async_generator():
"""
An async generator coroutine that yields random numbers between 0 and 10.
"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)

# Example of how to use the async generator
async def main():
    async for num in async_generator():
        print(num)

if __name__ == "__main__":
    asyncio.run(main())

