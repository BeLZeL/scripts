#!/usr/bin/env python3

'''
$ time ./coroutines.py 
Slow operation 1 complete
Slow operation 2 complete
Slow operation 3 complete

real    0m3,069s
user    0m0,064s
sys     0m0,000s
'''

import asyncio

async def slow_operation(n):
    await asyncio.sleep(n)
    print('Slow operation {} complete'.format(n))
    
async def main():
    await asyncio.wait([
        slow_operation(3),
        slow_operation(2),
        slow_operation(1),
    ])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
