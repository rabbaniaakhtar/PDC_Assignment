import threading
import time
import os
from random import randint

# Shared resources
primes = []
lock = threading.Lock()


# --- Prime helper functions ---
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_next_prime(start):
    """Find the next prime number greater than `start`."""
    n = start + 1
    while not is_prime(n):
        n += 1
    return n


# --- Thread Class Definition ---
class PrimeThread(threading.Thread):
    def __init__(self, name, limit):
        threading.Thread.__init__(self)
        self.name = name
        self.limit = limit

    def run(self):
        with lock:  # Acquire and release automatically
            print(f"--> {self.name} running in process ID {os.getpid()}")
            num = randint(1, 20)
            while num < self.limit:
                next_prime = find_next_prime(num)
                primes.append(next_prime)
                print(f"{self.name} produced prime {next_prime}")
                num = next_prime
                time.sleep(1)
            print(f"--> {self.name} completed.\n")


# --- Main Function ---
def main():
    start_time = time.time()

    # Create multiple threads
    threads = []
    for i in range(1, 6):
        t = PrimeThread(f"PrimeThread#{i}", limit=50)
        threads.append(t)

    # Start threads
    for t in threads:
        t.start()

    # Wait for all to finish
    for t in threads:
        t.join()

    # Print summary
    print("\nAll threads finished.")
    print(f"Total primes generated: {len(primes)}")
    print("Prime numbers:", primes)
    print(f"--- {time.time() - start_time:.2f} seconds ---")


if __name__ == "__main__":
    main()
