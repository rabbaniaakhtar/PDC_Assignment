# run_test.py

from prime_task import do_something  # Import the task
import time
import multiprocessing
import threading

if __name__ == "__main__":
    size = 1000      # How much work each process/thread does
    procs = 10       # Number of processes or threads

    # ----------- Multiprocessing -----------
    jobs = []
    start_time = time.time()

    for _ in range(procs):
        out_list = multiprocessing.Manager().list()
        process = multiprocessing.Process(target=do_something, args=(size, out_list))
        jobs.append(process)

    for job in jobs:
        job.start()
    for job in jobs:
        job.join()

    print("Multiprocessing complete.")
    print("Time taken:", time.time() - start_time)

    # ----------- Multithreading -----------
    jobs = []
    start_time = time.time()

    for _ in range(procs):
        out_list = []
        thread = threading.Thread(target=do_something, args=(size, out_list))
        jobs.append(thread)

    for job in jobs:
        job.start()
    for job in jobs:
        job.join()

    print("Multithreading complete.")
    print("Time taken:", time.time() - start_time)
