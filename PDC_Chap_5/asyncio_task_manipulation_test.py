import asyncio
from math_task import do_something

async def cube_sum_task(count):
    results = []
    print(f"Asyncio.Task: computing sum of cubes (count={count})")
    do_something(count, results)
    await asyncio.sleep(1)
    print(f"Asyncio.Task - sum of cubes({count}) = {results[0]}")

async def main():
    task_list = [
        asyncio.create_task(cube_sum_task(5)),
        asyncio.create_task(cube_sum_task(8)),
        asyncio.create_task(cube_sum_task(12))
    ]
    await asyncio.wait(task_list)

if __name__ == "__main__":
    asyncio.run(main())
