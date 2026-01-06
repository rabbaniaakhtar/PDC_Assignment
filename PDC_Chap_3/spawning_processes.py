import multiprocessing

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Worker function for each process
def prime_worker(i):
    print(f'Calling prime_worker from process №: {i}')
    start = i * 10 + 1     # Range start based on process number
    end = start + 9        # Range of 10 numbers
    print(f'Process {i} checking range {start} to {end}')

    for num in range(start, end + 1):
        if is_prime(num):
            print(f'Process {i}: {num} is a prime number')
    print(f'Process {i} finished.\n')


if __name__ == '__main__':
    print("Main process started.\n")

    # Launch 6 processes (like your myFunc example)
    for i in range(6):
        process = multiprocessing.Process(target=prime_worker, args=(i,))
        process.start()
        process.join()   # Wait for each process to finish before starting next

    print("\nMain process finished all prime checks.")
