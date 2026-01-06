Parallel and Distributed Computing – Chp 5

Chapter Objective

This chapter focuses on learning how Python handles asynchronous execution, task scheduling, and parallel processing. Using asyncio and concurrent.futures, the programs show how multiple tasks can run at the same time, share data safely, and improve execution efficiency compared to sequential programs.

Tools and Technologies

Programming Language: Python 3.11 or later

Libraries Used: asyncio, concurrent.futures, random, time

Development Environment: Visual Studio Code

Project Directory Layout
PDC-Chap5/
│ math_task.py
│ asyncio_futures_test.py
│ asyncio_coroutine_test.py
│ asyncio_eventloop_test.py
│ asyncio_task_manipulation_test.py
│ concurrent_futures_test.py
│ README.md

Description of Files
math_task.py

Purpose:
Defines the function do_something(count, out_list) which generates random numbers and calculates the cube of each value.

Concept:
This file represents a CPU-intensive task and is reused in all other programs to demonstrate parallel and asynchronous execution.

Working:
A specified number of random values are generated, their cubes are summed, and the final result is stored in a shared list.

Output:
Shows the calculated sum of cubes.

asyncio_futures_test.py

Purpose:
Illustrates asynchronous computation using asyncio Futures along with callback functions.

Concept:
A Future holds a result that becomes available later, while callbacks are triggered automatically once the task completes.

Working:
The CPU-bound function is executed asynchronously, Futures store the output, and callback functions display results after completion.

Output:
Each task prints its computed sum once finished.

asyncio_coroutine_test.py

Purpose:
Implements an asynchronous Finite State Machine (FSM) using coroutines.

Concept:
Each coroutine acts as a state, and control shifts between states using await statements until the final state is reached.

Working:
Execution starts from an initial state and randomly transitions through computation and verification states before producing the final output.

Output:
Logs state transitions and displays the final cube sum.

asyncio_eventloop_test.py

Purpose:
Demonstrates scheduling tasks directly on the event loop without using coroutines.

Concept:
Functions can be queued to execute immediately or after a delay using event loop scheduling methods.

Working:
Multiple tasks continuously schedule each other, and execution stops automatically after a fixed time.

Output:
Messages from different tasks printed repeatedly until the loop ends.

asyncio_task_manipulation_test.py

Purpose:
Shows how multiple asynchronous tasks can be launched and managed simultaneously.

Concept:
asyncio.create_task() allows several tasks to run concurrently inside the same event loop.

Working:
Several async wrappers execute the same computation in parallel, and results are collected once all tasks finish.

Output:
Displays results from all tasks in non-deterministic order.

concurrent_futures_test.py

Purpose:
Compares sequential execution with multithreading and multiprocessing.

Concept:

Thread pools work best for I/O-heavy workloads

Process pools are suitable for CPU-heavy tasks

Working:
The program runs the same function sequentially, then using a thread pool, and finally using a process pool while measuring execution time.

Output:
Shows task results and time comparison for all execution modes.

Final Summary

These programs collectively demonstrate how Python supports concurrency and parallelism. The asyncio module enables non-blocking task execution and structured asynchronous workflows. Task-based concurrency allows multiple operations to progress together, while concurrent.futures provides true parallelism through threads and processes. Together, these approaches improve responsiveness, optimize CPU usage, and handle multiple tasks efficiently.

Execution Instructions

To run any program, use the terminal command:

python filename.py


Example:

python asyncio_futures_test.py
