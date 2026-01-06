import concurrent.futures
import time
from math_task import do_something

count_list = [5, 8, 10, 12, 15]  # different task counts


def run_task(count):
    results = []
    do_something(count, results)
    print(f"Task with count={count}, sum of cubes={results[0]}")


if __name__ == "__main__":
    # Sequential Execution
    start_time = time.time()
    for count in count_list:
        run_task(count)
    print(f"Sequential Execution in {time.time() - start_time:.2f} seconds\n")

    # Thread Pool Execution
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for count in count_list:
            executor.submit(run_task, count)
    print(f"Thread Pool Execution in {time.time() - start_time:.2f} seconds\n")

    # Process Pool Execution
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        for count in count_list:
            executor.submit(run_task, count)
    print(f"Process Pool Execution in {time.time() - start_time:.2f} seconds\n")
