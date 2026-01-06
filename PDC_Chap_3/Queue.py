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


# Producer Process — generates numbers and adds them to queue
class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        print("Producer started...")
        for num in range(1, 21):  # produce numbers from 1 to 20
            self.queue.put(num)
            print(f"Producer: Number {num} added to queue")
            time.sleep(0.5)
        print("Producer finished producing.")
        self.queue.put(None)  # Sentinel value to tell consumer to stop


# Consumer Process — gets numbers from queue and checks for prime
class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        print("Consumer started...")
        while True:
            num = self.queue.get()
            if num is None:  # Sentinel value — end signal
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

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("Main Process Ended.")
