Multiprocessing vs. Multithreading in Python

This code demonstrates the difference in performance between multiprocessing and multithreading in Python when performing CPU-bound tasks.

The task used here is finding prime numbers up to a limit (1000) repeatedly, which is a CPU-intensive operation.

Python’s Global Interpreter Lock (GIL) prevents true parallel execution of threads for CPU tasks — so this experiment helps visualize the performance impact of that limitation.
        Code Explanation

1. `is_prime(n)`

Checks if a number is prime.

python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

 2. `find_primes_up_to(limit)`

Generates all prime numbers up to a given limit.

python
def find_primes_up_to(limit):
    return [num for num in range(limit) if is_prime(num)]


 3. `do_something(count, out_list)`

Repeats the prime-finding operation multiple times and stores results.

python
def do_something(count, out_list):
    limit = 1000  # Find all primes up to this number
    for _ in range(count):
        primes = find_primes_up_to(limit)
        out_list.append(len(primes))

 4. Main Execution

Runs the same workload using:

* Multiprocessing (multiple processes)
* Multithreading (multiple threads)

python
if __name__ == "__main__":
    size = 1000      # Work done by each process/thread
    procs = 10       # Number of processes/threads

Each section measures the time taken to complete the same number of operations using both approaches.


 Output Results

Test Results Summary

| Processes/Threads | Multiprocessing Time (s) | Multithreading Time (s) |
| ----------------: | -----------------------: | ----------------------: |
|                10 |                     5.97 |                   16.28 |
|                15 |                     6.91 |                   23.45 |
|                20 |                     9.32 |                   30.22 |


 Analysis

* As the number of workers increases, multiprocessing scales better and remains relatively efficient.
* Multithreading, on the other hand, performs worse as threads increase, due to Python’s Global Interpreter Lock (GIL) preventing true parallel CPU execution.

 Conclusion

* Multiprocessing is ideal for CPU-bound tasks (e.g., number crunching, data processing) because each process runs on a separate CPU core.
* Multithreading is better suited for I/O-bound tasks (e.g., network requests, file operations) where threads spend time waiting.

Final Verdict:

 For CPU-intensive operations like prime number calculation, multiprocessing significantly outperforms multithreading in Python.

 How to Run

1. Save the script as `prime_task.py`
2. Run using:

    bash
   python prime_task.py
   
3. Compare the execution times printed for both multiprocessing and multithreading.
