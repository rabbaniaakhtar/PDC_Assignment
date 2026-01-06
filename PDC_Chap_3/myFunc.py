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


# Worker function similar to myFunc()
def myFunc(i):
    print(f'\nCalling myFunc from process n°: {i}')
    for num in range(1, i + 1):
        if is_prime(num):
            print(f'Process {i} → {num} is a Prime number')
        else:
            print(f'Process {i} → {num} is NOT a Prime number')
        time.sleep(0.2)  # Just to slow down for demo
    print(f'Process {i} finished execution\n')


if __name__ == '__main__':
    print("Main Process Started\n")

    # Create multiple processes — each running myFunc with different ranges
    processes = []
    for i in range(3, 8):  # 5 processes with different ranges
        p = multiprocessing.Process(target=myFunc, args=(i,))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("\nAll processes finished. Main process ended.")
