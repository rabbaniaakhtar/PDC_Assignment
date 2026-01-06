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


# Each process will execute this function
def find_primes_in_range(start, end):
    name = multiprocessing.current_process().name
    print(f"Starting {name}\n")

    for num in range(start, end + 1):
        if is_prime(num):
            print(f"{name}: {num} is a prime number")

    time.sleep(1)
    print(f"Exiting {name}\n")


if __name__ == '__main__':
    # Define the range of numbers to check
    total_range = (1, 50)
    mid_point = (total_range[1] - total_range[0]) // 2 + total_range[0]

    # First half handled by "background_process"
    background_process = multiprocessing.Process(
        name='background_process',
        target=find_primes_in_range,
        args=(total_range[0], mid_point)
    )
    background_process.daemon = False  # Run as a regular process

    # Second half handled by "NO_background_process"
    NO_background_process = multiprocessing.Process(
        name='NO_background_process',
        target=find_primes_in_range,
        args=(mid_point + 1, total_range[1])
    )
    NO_background_process.daemon = False

    # Start both processes
    background_process.start()
    NO_background_process.start()

    # Wait for both to finish
    background_process.join()
    NO_background_process.join()

    print("\nBoth processes have finished checking for prime numbers.")
