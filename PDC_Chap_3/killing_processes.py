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


# Producer Process — generates numbers
class Producer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        print("Producer started...")
        for num in range(1, 21):  # numbers 1 to 20
            self.queue.put(num)
            print(f"Producer: Number {num} added to queue")
            time.sleep(0.5)
        print("Producer finished producing.")
        self.queue.put(None)  # Sentinel to stop consumer


# Consumer Process — consumes numbers and checks primes
class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        print("Consumer started...")
        while True:
            num = self.queue.get()
            if num is None:  # End signal
                print("Consumer finished consuming.")
                break

            if is_prime(num):
                print(f"Consumer: {num} is a Prime number")
            else:
                print(f"Consumer: {num} is NOT a Prime number")

            time.sleep(1)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    producer = Producer(queue)
    consumer = Consumer(queue)

    # Process status before starting
    print("Before start:")
    print("Producer:", producer, "Alive:", producer.is_alive())
    print("Consumer:", consumer, "Alive:", consumer.is_alive())

    # Start processes
    producer.start()
    consumer.start()

    print("\nAfter start:")
    print("Producer:", producer, "Alive:", producer.is_alive())
    print("Consumer:", consumer, "Alive:", consumer.is_alive())

    # Let processes run for a while
    time.sleep(3)

    # Terminate the producer early (for demo)
    producer.terminate()
    print("\nProducer terminated!")
    print("Producer alive:", producer.is_alive())

    # Wait for processes to finish
    producer.join()
    consumer.join()

    # Final process status
    print("\nAfter join:")
    print("Producer:", producer, "Alive:", producer.is_alive(), "Exit code:", producer.exitcode)
    print("Consumer:", consumer, "Alive:", consumer.is_alive(), "Exit code:", consumer.exitcode)

    print("\nMain Process Ended.")
