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


def prime_worker(start, end):
    name = multiprocessing.current_process().name
    print(f"Starting {name}\n")

    if name == 'background_process':
        # Daemon process (background)
        for num in range(start, end + 1):
            if is_prime(num):
                print(f"{name}: {num} is a prime number")
            time.sleep(0.2)
    else:
        # Non-daemon process (foreground)
        for num in range(start, end + 1):
            if is_prime(num):
                print(f"{name}: {num} is a prime number")
            time.sleep(0.2)

    print(f"Exiting {name}\n")


if __name__ == '__main__':
    print("Main process started.\n")

    # Create one daemon and one non-daemon process
    background_process = multiprocessing.Process(
        name='background_process',
        target=prime_worker,
        args=(1, 15)
    )
    background_process.daemon = True  # Ends when main process ends

    NO_background_process = multiprocessing.Process(
        name='NO_background_process',
        target=prime_worker,
        args=(16, 30)
    )
    NO_background_process.daemon = False  # Keeps running until finished

    # Start both processes
    background_process.start()
    NO_background_process.start()

    # Join only the non-daemon process (daemon will stop automatically)
    NO_background_process.join()

    print("\nMain process exiting — daemon process will terminate automatically.")
