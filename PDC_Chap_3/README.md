 Python Multiprocessing — Prime Number Examples

 Overview

This chapter demonstrates various multiprocessing techniques in Python using the prime number calculation as a base example.
Each version showcases a different multiprocessing concept such as `Process`, `Queue`, `Pipe`, `Pool`, `Barrier`, and `Daemon`.


 Requirements

Make sure you have Python 3 installed.

```bash
python --version
```

No external libraries are required — only the built-in `multiprocessing`, `time`, and `random` modules are used.

---
 Code Variants & Concepts

1. Basic Prime Number Functions

* `is_prime(n)`: checks if a number is prime.
* `find_primes_up_to(limit)`: returns all prime numbers up to the given limit.

These functions are reused across all multiprocessing examples.

2. Multiprocessing with Queues

File: `Queue.py`

Concept:
Producer and Consumer processes communicate via a `multiprocessing.Queue`.

* Producer generates random numbers and adds them to the queue.
* Consumer retrieves numbers and checks if they are prime.

Use Case: Demonstrates inter-process communication using a shared queue.

---

3. Multiprocessing with Pipes**

File: `Pipe.py`

Concept:
Processes communicate directly using a `Pipe`.

* The first process sends numbers through a pipe.
* The second process receives numbers and calculates if they are prime.

Use Case: Shows how to transfer data directly between two processes.

---

4. Process Creation and Termination**

File: `killing_processes.py`

Concept:
Demonstrates how to start, terminate, and join processes.

* A process runs the prime function but is terminated before completion.
* Shows the lifecycle states: before start, running, terminated, and joined.

---

5. Custom Process Class**

File: `myFunc.py`

Concept:
Subclassing `multiprocessing.Process` to create custom behavior.

* A class `MyProcess` overrides the `run()` method to perform prime number checks.
* Multiple instances are launched and synchronized using `.start()` and `.join()`.

---

6. Multiprocessing Pool**

File: `process_pool.py`

Concept:
Using a `multiprocessing.Pool` to run many tasks in parallel.

* Distributes prime-checking tasks among multiple worker processes.
* `pool.map()` is used to process multiple numbers concurrently.

Use Case: Efficient when dealing with large sets of numbers.

---

7. Barrier Synchronization**

File: `processes_barrier.py`

Concept:
Synchronize processes so that they start a specific task at the same time.

* Uses `multiprocessing.Barrier` and `Lock`.
* Prime calculation begins only when all processes reach the barrier point.

Use Case: Coordinating multiple processes to start together.

---

8. Daemon vs Non-Daemon Processes**

File: `run_background_processes_no_daemons.py`

Concept:
Shows how background (daemon) processes behave compared to regular ones.

* `background_process` runs prime checks in the first half of a range.
* `NO_background_process` runs in the second half.
* Both execute concurrently, but daemons terminate when the main process ends.

---

9. Sequential Multi-Process Execution**

File: `spawning_processes.py`

Concept:
Spawns multiple processes one after another, each working on a different range of numbers.

* Similar to your `myFunc(i)` example.
* Each process computes primes in its own small range.

Use Case: Sequential process creation for controlled parallelism.

---

10. Barrier Example Combined with Prime Numbers**

File: `run_background_processes_no_daemons.py`

Concept:
Two processes wait at a synchronization point before printing prime numbers with timestamps.

Use Case: Understanding synchronized execution timing.

---

 Example Output (Prime Pool Version)

```
Prime Check Results:

1 is NOT a Prime number
2 is a Prime number
3 is a Prime number
4 is NOT a Prime number
5 is a Prime number
...
47 is a Prime number
48 is NOT a Prime number
49 is NOT a Prime number
50 is NOT a Prime number
```

---

 Key Learnings

| Concept               | Module Used               | Description                                 |
| --------------------- | ------------------------- | ------------------------------------------- |
| Basic multiprocessing | `multiprocessing.Process` | Creating and managing processes             |
| Communication         | `Queue`, `Pipe`           | Sending data between processes              |
| Synchronization       | `Barrier`, `Lock`         | Coordinating process execution              |
| Process Pool          | `Pool`                    | Managing a pool of worker processes         |
| Daemon                | `daemon` flag             | Running background processes                |
| Joining               | `.join()`                 | Ensuring processes finish before continuing |

---


To run any version:

```bash
python filename.py
```

For example:

```bash
python prime_pool.py
```
