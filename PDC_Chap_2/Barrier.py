from threading import Barrier, Thread
from time import ctime, sleep
from random import randrange

# --- Prime Number Functions ---
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_up_to(limit):
    return [num for num in range(limit) if is_prime(num)]


def do_something(count, out_list):
    limit = 1000  
    for _ in range(count):
        primes = find_primes_up_to(limit)
        out_list.append(len(primes))


# --- Threading and Barrier Part ---
num_threads = 3
finish_line = Barrier(num_threads)
results = []

def prime_worker(name):
    print(f"{name} started calculating primes at {ctime()}")
    sleep(randrange(1, 4))  # simulate time variation
    local_results = []
    do_something(2, local_results)
    print(f"{name} finished calculations at {ctime()} with results: {local_results}")
    
    print(f"{name} waiting at the barrier...\n")
    finish_line.wait()  # barrier point
    print(f"{name} passed the barrier at {ctime()}!\n")


def main():
    print("=== PRIME NUMBER THREAD RACE STARTED ===")
    threads = []
    names = ['Thread-A', 'Thread-B', 'Thread-C']
    
    for name in names:
        t = Thread(target=prime_worker, args=(name,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    print("=== All threads finished. Race over! ===")


if __name__ == "__main__":
    main()
