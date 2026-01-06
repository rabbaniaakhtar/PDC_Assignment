import asyncio
import random
import sys
from math_task import do_something

async def task_coroutine(future, count):
    result_list = []
    do_something(count, result_list)
    await asyncio.sleep(1)
    future.set_result(f"Sum of cubes for count={count} is {result_list[0]}")

def got_result(future):
    print(future.result())

async def main(count1, count2):
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    tasks = [
        asyncio.create_task(task_coroutine(future1, count1)),
        asyncio.create_task(task_coroutine(future2, count2))
    ]

    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    await asyncio.wait(tasks)

if __name__ == "__main__":
    count1 = int(sys.argv[1])
    count2 = int(sys.argv[2])
    asyncio.run(main(count1, count2))
