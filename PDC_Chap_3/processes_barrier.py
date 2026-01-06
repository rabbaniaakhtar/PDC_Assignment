import multiprocessing
from multiprocessing import Barrier, Lock, Process
from datetime import datetime
from time import time, sleep

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Each process will wait at the barrier, then start checking primes
def prime_worker(start, end, synchronizer, serializer):
    name = multiprocessing.current_process().name

    # All processes wait here until everyone reaches the barrier
    synchronizer.wait()

    now = datetime.fromtimestamp(time())
    with serializer:
        print(f"\n{name} started at {now}")
        print(f"{name} is checking primes from {start} to {end}\n")

    # Perform prime checking
    for num in range(start, end + 1):
        if is_prime(num):
            with serializer:
                print(f"{name}: {num} is a Prime number")
        sleep(0.1)

    with serializer:
        print(f"\n{name} finished at {datetime.fromtimestamp(time())}\n")


if __name__ == '__main__':
    print("Main process started.\n")

    # Synchronization primitives
    synchronizer = Barrier(3)  # 3 processes must reach the barrier
    serializer = Lock()

    # Create processes — each checks a different number range
    p1 = Process(name='Process-1', target=prime_worker, args=(1, 10, synchronizer, serializer))
    p2 = Process(name='Process-2', target=prime_worker, args=(11, 20, synchronizer, serializer))
    p3 = Process(name='Process-3', target=prime_worker, args=(21, 30, synchronizer, serializer))

    # Start all processes
    p1.start()
    p2.start()
    p3.start()

    # Wait for all to finish
    p1.join()
    p2.join()
    p3.join()

    print("\nAll processes finished. Main process ended.")
