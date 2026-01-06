import asyncio
import time
from random import randint
from math_task import do_something

async def start_state(count):
    print("Start State\n")
    await asyncio.sleep(1)

    branch = randint(0, 1)
    if branch == 0:
        result = await compute_state(count)
    else:
        result = await alternate_state(count)

    print("Resume Transition:\nStart State calling\n" + result)

async def compute_state(count):
    output = "Compute State\n"
    results = []
    do_something(count, results)
    await asyncio.sleep(1)

    print("...evaluating...")
    branch = randint(0, 1)
    if branch == 0:
        result = await verify_state(results[0])
    else:
        result = await end_state(results[0])

    return output + "Compute State calling\n" + result

async def alternate_state(count):
    output = "Alternate State\n"
    results = []
    do_something(count, results)
    await asyncio.sleep(1)

    print("...evaluating...")
    result = await verify_state(results[0])
    return output + "Alternate State calling\n" + result

async def verify_state(value):
    output = f"Verify State: value={value}\n"
    await asyncio.sleep(1)
    print("...evaluating...")
    return output + (await end_state(value))

async def end_state(value):
    print("...stop computation...")
    return f"End State: Final Sum of Cubes = {value}\n"

if __name__ == "__main__":
    asyncio.run(start_state(5))
