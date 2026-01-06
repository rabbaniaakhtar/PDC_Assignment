 Python Multithreading Synchronization Examples

 Overview

This project demonstrates 7 synchronization techniques in Python multithreading, each implemented with a practical example.
The goal is to understand how threads coordinate, communicate, and control shared resources safely.

Each program builds on the same concepts — threading, synchronization, and shared data — but uses different thread coordination mechanisms such as:

* Barrier
* Condition
* Event
* Lock
* RLock (Reentrant Lock)
* Semaphore
* Queue (Producer–Consumer)


 1. Barrier Example

 File: `Barrier.py`

Concept: Threads wait for each other at a common barrier point before continuing.

Summary:

* Multiple threads compute prime numbers up to a limit.
* All threads must reach the barrier before proceeding to print completion.
* Simulates a race where all participants wait for others at the finish line.

Key Function: `threading.Barrier()`


 2. Condition Example

 File: `Condition.py`

Concept: Used for thread communication based on a condition being met.

Summary:

* Producer generates prime numbers and notifies Consumer threads.
* Consumers wait (`condition.wait()`) until notified that new primes are available.
* Demonstrates precise control of wait/notify logic.

Key Function: `threading.Condition()`


 3. Event Example

 File: `Event.py`

Concept: One thread signals an event to allow others to proceed.

Summary:

* The Producer thread sets an event when a new prime number is generated.
* The Consumer thread waits (`event.wait()`) for that signal to process the prime.
* Simulates asynchronous signaling between threads.

Key Function: `threading.Event()`


 4. Lock Example

 File: `Lock.py`

Concept: Prevents multiple threads from modifying shared data simultaneously.

Summary:

* Each thread calculates and prints prime numbers with a lock acquired.
* The lock ensures that only one thread prints or updates shared data at a time.
* Avoids race conditions.

Key Function: `threading.Lock()`


  5. RLock (Reentrant Lock) Example

 File: `Rlock.py`

Concept: A thread can re-acquire the same lock multiple times safely.

Summary:

* Demonstrates nested locking during prime number addition/removal operations.
* Simulates a shared “Box” where items (primes) are added and removed.
* Reentrant lock prevents self-deadlock when the same thread needs the lock again.

Key Function: `threading.RLock()`


 6. Semaphore Example

 File: `Semaphore.py`

Concept: Controls access to a shared resource through a counter.

Summary:

* Producer releases a semaphore when a new prime is ready.
* Consumer acquires the semaphore before processing it.
* Limits the number of threads accessing a shared resource simultaneously.

Key Function: `threading.Semaphore()`


 7. Queue Example

 File: `Queue.py`

Concept: Thread-safe data exchange between producers and consumers.

Summary:

* Producer thread puts numbers in a shared queue.
* Multiple Consumers pull numbers and check if they are prime.
* Graceful termination with `None` signals for consumers.
* Safest and most efficient way to manage producer–consumer workflows.

Key Function: `queue.Queue()`


 Common Concepts Across All Codes

| Concept              | Description                                                   |
| -------------------- | ------------------------------------------------------------- |
| **Thread Creation**  | Each class extends `threading.Thread` and overrides `run()`   |
| **Synchronization**  | Ensures threads cooperate correctly using various primitives  |
| **Shared Resource**  | A list, counter, or queue is used to demonstrate coordination |
| **Thread Safety**    | Prevents race conditions and deadlocks                        |
| **Logging/Printing** | Displays thread actions to visualize synchronization behavior |


 Learning Outcomes

After running these programs, you will:

* Understand the differences between synchronization primitives in Python.
* Know when to use `Lock`, `RLock`, `Semaphore`, or `Condition`.
* Learn how to coordinate multiple threads using `Event`, `Barrier`, and `Queue`.
* Build safer and more efficient concurrent applications.


 How to Run

1. Save each file separately (`Barrier.py`, `Condition.py`, etc.).
2. Run in terminal or any IDE:

   ```bash
   python Barrier.py
   
3. Observe how threads interact — waiting, signaling, or locking.


 Example Directory Structure


multithreading_synchronization/
│
├── barrier_prime.py
├── condition_prime.py
├── event_prime.py
├── lock_prime.py
├── rlock_prime.py
├── semaphore_prime.py
├── queue_prime.py
└── README.md


