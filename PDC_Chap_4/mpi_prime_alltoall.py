from mpi4py import MPI
import numpy

# ---------- Prime Number Functions ----------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_up_to(limit):
    return [num for num in range(limit) if is_prime(num)]


def do_something(count, out_list):
    limit = 1000  # Find all primes up to this number
    for _ in range(count):
        primes = find_primes_up_to(limit)
        out_list.append(len(primes))  # store how many primes were found


# ---------- MPI Communication Setup ----------
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Each process computes some primes
results = []
do_something(1, results)
prime_count = results[0]  # how many primes found

# Each process prepares data for Alltoall
# For demonstration, multiply prime_count by (rank+1)
senddata = (rank + 1) * numpy.arange(size, dtype=int)
recvdata = numpy.empty(size, dtype=int)

# Exchange data among all processes
comm.Alltoall(senddata, recvdata)

# Print results for each process
print(f"Process {rank}: Found {prime_count} primes up to 1000")
print(f"Process {rank} sending {senddata} receiving {recvdata}\n")
