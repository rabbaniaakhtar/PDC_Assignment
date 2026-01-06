import multiprocessing

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Function executed by each process in the pool
def check_prime(num):
    if is_prime(num):
        return f"{num} is a Prime number"
    else:
        return f"{num} is NOT a Prime number"


if __name__ == '__main__':
    # Create input data — numbers 1 to 50
    numbers = list(range(1, 51))

    # Create a pool with 4 worker processes
    pool = multiprocessing.Pool(processes=4)

    # Distribute tasks among the pool
    results = pool.map(check_prime, numbers)

    # Close and join the pool
    pool.close()
    pool.join()

    # Display the results
    print("\nPrime Check Results:\n")
    for res in results:
        print(res)
