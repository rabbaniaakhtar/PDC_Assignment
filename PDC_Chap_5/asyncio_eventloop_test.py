import asyncio
import time
import random
from math_task import do_something


def task_A(end_time, loop, count):
    print("Task A: generating cube sum")
    results = []
    do_something(count, results)

    time.sleep(random.randint(0, 3))

    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_B, end_time, loop, results[0])
    else:
        loop.stop()


def task_B(end_time, loop, value):
    print(f"Task B: received value = {value}")
    time.sleep(random.randint(0, 3))

    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_C, end_time, loop, value)
    else:
        loop.stop()


def task_C(end_time, loop, value):
    print(f"Task C: final processing of value = {value}")
    time.sleep(random.randint(0, 3))

    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_A, end_time, loop, random.randint(3, 8))
    else:
        loop.stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    end_loop = loop.time() + 30  # run for 30 seconds

    loop.call_soon(task_A, end_loop, loop, 5)
    loop.run_forever()
    loop.close()
