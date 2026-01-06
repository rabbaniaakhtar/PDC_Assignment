import threading
import time
import random


# --- Class with RLock for shared access ---
class PrimeBox:
    def __init__(self):
        self.lock = threading.RLock()
        self.primes = []

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_next_prime(self, start):
        n = start + 1
        while not self.is_prime(n):
            n += 1
        return n

    def execute(self, prime):
        """Internal method that modifies shared data."""
        with self.lock:
            self.primes.append(prime)

    def add_prime(self):
        """Find and add next prime."""
        with self.lock:
            start = random.randint(1, 30)
            next_prime = self.find_next_prime(start)
            self.execute(next_prime)
            print(f"Added prime: {next_prime}, total primes: {len(self.primes)}")

    def remove_prime(self):
        """Remove last prime."""
        with self.lock:
            if self.primes:
                removed = self.primes.pop()
                print(f"Removed prime: {removed}, remaining: {len(self.primes)}")
            else:
                print("No primes to remove.")


# --- Thread functions ---
def adder(box, items):
    print(f"N° {items} primes to ADD\n")
    while items:
        box.add_prime()
        time.sleep(1)
        items -= 1
        print(f"ADDED one prime --> {items} left to ADD\n")


def remover(box, items):
    print(f"N° {items} primes to REMOVE\n")
    while items:
        box.remove_prime()
        time.sleep(1.5)
        items -= 1
        print(f"REMOVED one prime --> {items} left to REMOVE\n")


# --- Main function ---
def main():
    box = PrimeBox()
    adder_count = random.randint(5, 10)
    remover_count = random.randint(3, 6)

    t1 = threading.Thread(target=adder, args=(box, adder_count))
    t2 = threading.Thread(target=remover, args=(box, remover_count))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nFinal primes list:", box.primes)
    print("Execution complete.")


if __name__ == "__main__":
    main()
