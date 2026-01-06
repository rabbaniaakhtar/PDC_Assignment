import multiprocessing
import time

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Producer process: generates numbers
def producer_func(queue):
    name = multiprocessing.current_process().name
    print(f"Starting process name = {name}\n")
    for num in range(1, 21):
        queue.put(num)
        print(f"{name}: Added number {num} to queue")
        time.sleep(0.3)
    queue.put(None)  # Sentinel value to stop consumer
    print(f"Exiting process name = {name}\n")


# Consumer process: checks primes
def consumer_func(queue):
    name = multiprocessing.current_process().name
    print(f"Starting process name = {name}\n")
    while True:
        num = queue.get()
        if num is None:
            print(f"Exiting process name = {name}\n")
            break

        if is_prime(num):
            print(f"{name}: {num} is a Prime number")
        else:
            print(f"{name}: {num} is NOT a Prime number")
        time.sleep(0.5)


if __name__ == '__main__':
    queue = multiprocessing.Queue()

    # Create processes with custom names
    process_with_name = multiprocessing.Process(
        name='Prime Producer',
        target=producer_func,
        args=(queue,)
    )

    process_with_default_name = multiprocessing.Process(
        name='Prime Checker',
        target=consumer_func,
        args=(queue,)
    )

    # Start both processes
    process_with_name.start()
    process_with_default_name.start()

    # Wait for both to complete
    process_with_name.join()
    process_with_default_name.join()

    print("\nMain process ended.")
