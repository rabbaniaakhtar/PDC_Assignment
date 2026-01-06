import logging
import threading
import time
import random

# Logging setup
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared resources
primes = []
event = threading.Event()


# --- Prime helper functions ---
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_next_prime(start):
    """Find the next prime greater than `start`."""
    n = start + 1
    while not is_prime(n):
        n += 1
    return n


# --- Producer Thread (generates primes) ---
class PrimeProducer(threading.Thread):
    def __init__(self, limit, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.limit = limit

    def run(self):
        num = 1
        while num < self.limit:
            next_prime = find_next_prime(num)
            primes.append(next_prime)
            logging.info(f'Producer: produced prime {next_prime}')
            event.set()      # signal that a new item is ready
            event.clear()    # reset event for the next cycle
            num = next_prime
            time.sleep(random.uniform(1, 2))  # simulate work delay


# --- Consumer Thread (uses primes) ---
class PrimeConsumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            event.wait()  # wait for producer to signal
            if primes:
                item = primes.pop(0)
                logging.info(f'Consumer: consumed prime {item}')
            else:
                logging.info('Consumer: no primes to consume')
            time.sleep(random.uniform(1, 2))


# --- Main function ---
def main():
    producer = PrimeProducer(limit=50, name='Producer')
    consumer = PrimeConsumer(name='Consumer')

    producer.start()
    consumer.start()

    producer.join()
    # Consumer runs indefinitely, so you might not join it here
    # In a real program, you could stop it with a flag


if __name__ == "__main__":
    main()
