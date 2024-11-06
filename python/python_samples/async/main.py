#!/usr/bin/env python3

import asyncio

async def slow_operation(n):
    print(f"Function {n} is running")
    await asyncio.sleep(n)
    print(f"Function {n} is done")
    return f"Function {n}"

async def main():
    print("Main function is running")
    results = await asyncio.gather(
        slow_operation(3),
        slow_operation(2),
        slow_operation(1))
    print("Main function is done")
    print(results)

asyncio.run(main())
