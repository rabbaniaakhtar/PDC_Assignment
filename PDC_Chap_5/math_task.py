import random

def do_something(count, out_list):
    """Generates random numbers and computes the sum of their cubes."""
    total = 0
    for _ in range(count):
        num = random.randint(1, 100)
        total += num ** 3
    out_list.append(total)
