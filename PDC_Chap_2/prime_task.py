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