from threading import Thread
from queue import Queue
import time


# --- Function to check if number is prime ---
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# --- Producer Class ---
class Producer(Thread):
    def __init__(self, queue, numbers):
        Thread.__init__(self)
        self.queue = queue
        self.numbers = numbers

    def run(self):
        for num in self.numbers:
            print(f"Producer added number: {num}")
            self.queue.put(num)
            time.sleep(0.5)  # simulate delay

        # Signal to consumers that production is complete
        for _ in range(3):  # number of consumers
            self.queue.put(None)


# --- Consumer Class ---
class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            num = self.queue.get()
            if num is None:
                print(f"{self.name} exiting (no more numbers).")
                self.queue.task_done()
                break

            if is_prime(num):
                print(f"{self.name} → {num} is PRIME.")
            else:
                print(f"{self.name} → {num} is NOT prime.")

            time.sleep(1)
            self.queue.task_done()


# --- Main Execution ---
if __name__ == "__main__":
    queue = Queue()

    # List of numbers to check
    numbers = [2, 3, 4, 5, 10, 13, 15, 17, 19, 20]

    # Threads
    producer = Producer(queue, numbers)
    consumer1 = Consumer(queue)
    consumer2 = Consumer(queue)
    consumer3 = Consumer(queue)

    producer.start()
    consumer1.start()
    consumer2.start()
    consumer3.start()

    producer.join()
    queue.join()

    print("\n✅ All numbers processed successfully.")
