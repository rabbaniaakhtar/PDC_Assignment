import multiprocessing
import time

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Custom Producer Process class
class PrimeProducer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        print(f"Called run() method in {self.name} (Producer)")
        for num in range(1, 21):
            self.queue.put(num)
            print(f"{self.name}: Added number {num} to queue")
            time.sleep(0.3)
        self.queue.put(None)  # Sentinel to stop consumer
        print(f"{self.name}: Finished producing\n")


# Custom Consumer Process class
class PrimeConsumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        print(f"Called run() method in {self.name} (Consumer)")
        while True:
            num = self.queue.get()
            if num is None:
                print(f"{self.name}: No more items, exiting...\n")
                break

            if is_prime(num):
                print(f"{self.name}: {num} is a Prime number")
            else:
                print(f"{self.name}: {num} is NOT a Prime number")
            time.sleep(0.5)


if __name__ == '__main__':
    queue = multiprocessing.Queue()

    # Create producer and consumer process objects
    producer = PrimeProducer(queue)
    consumer = PrimeConsumer(queue)

    # Start processes
    producer.start()
    consumer.start()

    # Wait for completion
    producer.join()
    consumer.join()

    print("Main process ended.")
