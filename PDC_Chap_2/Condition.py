import threading
import time
import logging

# --- Logging format setup ---
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared data
primes = []
condition = threading.Condition()
MAX_SIZE = 5  # max primes in list at a time


# --- Prime functions ---
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_next_prime(start):
    """Find next prime number greater than 'start'"""
    n = start + 1
    while not is_prime(n):
        n += 1
    return n


# --- Producer Thread ---
class PrimeProducer(threading.Thread):
    def __init__(self, limit, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.limit = limit

    def produce(self):
        global primes
        num = 1
        while num < self.limit:
            next_prime = find_next_prime(num)
            with condition:
                while len(primes) >= MAX_SIZE:
                    logging.info('Buffer full, producer waiting...')
                    condition.wait()
                primes.append(next_prime)
                logging.info(f'Produced prime: {next_prime}, total buffer: {len(primes)}')
                condition.notify()
            num = next_prime
            time.sleep(1)

    def run(self):
        self.produce()


# --- Consumer Thread ---
class PrimeConsumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):
        global primes
        while True:
            with condition:
                while len(primes) == 0:
                    logging.info('No primes to consume, waiting...')
                    condition.wait()
                prime = primes.pop(0)
                logging.info(f'Consumed prime: {prime}, remaining: {len(primes)}')
                condition.notify()
            time.sleep(2)

    def run(self):
        self.consume()


# --- Main function ---
def main():
    producer = PrimeProducer(limit=50, name='Producer')
    consumer = PrimeConsumer(name='Consumer')

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()


if __name__ == "__main__":
    main()
