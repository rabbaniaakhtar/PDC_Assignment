import logging
import threading
import time
import random

# --- Logging setup ---
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# --- Shared resources ---
semaphore = threading.Semaphore(0)
primes = []
lock = threading.Lock()  # to protect shared list


# --- Helper functions ---
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_next_prime(start):
    n = start + 1
    while not is_prime(n):
        n += 1
    return n


# --- Producer function ---
def producer():
    for _ in range(5):  # produce 5 primes
        time.sleep(random.uniform(1, 3))
        start = random.randint(1, 50)
        next_prime = find_next_prime(start)
        with lock:
            primes.append(next_prime)
        logging.info(f'Producer generated prime: {next_prime}')
        semaphore.release()  # signal to consumer


# --- Consumer function ---
def consumer():
    for _ in range(5):  # consume 5 primes
        logging.info('Consumer waiting for prime...')
        semaphore.acquire()  # wait until producer signals
        with lock:
            prime = primes.pop(0)
        logging.info(f'Consumer got prime: {prime}')


# --- Main function ---
def main():
    t1 = threading.Thread(target=consumer, name='Consumer')
    t2 = threading.Thread(target=producer, name='Producer')

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    logging.info('All primes processed successfully!')


if __name__ == "__main__":
    main()
