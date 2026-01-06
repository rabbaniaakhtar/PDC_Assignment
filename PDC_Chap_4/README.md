 Prime Number Calculation with MPI Grid Topology

 Overview

This project demonstrates the use of MPI (Message Passing Interface) with Cartesian grid topology to perform distributed prime number computation.
Each MPI process is assigned a coordinate in a 2D grid, identifies its neighboring processes, and computes how many prime numbers exist up to a certain limit that depends on its position in the grid.

This helps illustrate both MPI topology management and parallel numeric computation.

---

 Features

* Uses `mpi4py` for parallel communication.
* Builds a **2D Cartesian grid** of MPI processes.
* Automatically determines each process’s **row and column**.
* Identifies **neighboring processes** in four directions:

  * `UP`, `DOWN`, `LEFT`, `RIGHT`
* Each process performs a **prime number count** up to a variable limit.
* Optionally supports periodic (wrap-around) grid behavior.

---
 How It Works

1. The total number of MPI processes (`size`) is used to form a 2D grid (`rows × columns`).
2. Each process obtains:

   * Its **rank** (unique process ID)
   * Its **(row, column)** coordinates in the grid
   * The ranks of its **neighboring processes**
3. The limit for prime calculation is adjusted based on the process’s grid coordinates:

   ```
   limit = 1000 + (row * 100) + (col * 50)
   ```
4. Each process counts the total number of primes up to its limit.
5. The program prints:

   * Process rank and coordinates
   * Neighbor ranks (UP, DOWN, LEFT, RIGHT)
   * Limit used
   * Total number of primes found

---
 Example Output

When run with **9 processes**, output might look like this (abbreviated):

```
Building a 3 x 3 grid topology:

Process 0 at Grid Position (Row=0, Col=0)
-------------------------------------
Neighbours:
   UP    = 6
   DOWN  = 3
   LEFT  = 2
   RIGHT = 1
Prime Calculation:
   Limit = 1000
   Total Primes Found = 168
```

Each process prints its own version with different coordinates and results.

---

 How to Run

 Prerequisites

Make sure you have:

* Python 3.8+
* mpi4py installed
  You can install it with:

  ```bash
  pip install mpi4py
  ```

 Run the Program

Save the file as:

```
prime_grid_topology.py
```

Run using mpiexec or mpirun:

```bash
mpiexec -n 9 python prime_grid_topology.py
```

> ⚠️ Make sure the number of processes (`-n`) forms a valid square grid (like 4, 9, 16, etc.) for a balanced topology.

---

 File Structure

```
prime_grid_topology.py   → Main Python file containing MPI logic and prime calculation
README.md                → Project documentation
```

---

 Technologies Used

* Python
* NumPy
* mpi4py (MPI for Python)

---

 Concepts Demonstrated

* MPI Initialization and Communication
* Cartesian Topology Creation (`Create_cart`)
* Neighbor Detection using `Shift`
* Distributed Computation (Prime Number Counting)
* Parallel Output per Process

---

 
