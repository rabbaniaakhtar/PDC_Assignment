import multiprocessing

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to generate numbers and send through pipe
def generate_numbers(pipe):
    output_pipe, _ = pipe
    for num in range(1, 21):  # send numbers from 1 to 20
        output_pipe.send(num)
    output_pipe.close()

# Function to receive numbers, check if prime, and send result
def process_primes(pipe_in, pipe_out):
    close, input_pipe = pipe_in
    close.close()
    output_pipe, _ = pipe_out
    try:
        while True:
            num = input_pipe.recv()
            if is_prime(num):
                output_pipe.send(f"{num} is Prime")
            else:
                output_pipe.send(f"{num} is Not Prime")
    except EOFError:
        output_pipe.close()

if __name__ == "__main__":
    # First pipe: generator → processor
    pipe_1 = multiprocessing.Pipe(True)
    p1 = multiprocessing.Process(target=generate_numbers, args=(pipe_1,))
    p1.start()

    # Second pipe: processor → main
    pipe_2 = multiprocessing.Pipe(True)
    p2 = multiprocessing.Process(target=process_primes, args=(pipe_1, pipe_2))
    p2.start()

    # Close unused ends in main
    pipe_1[0].close()
    pipe_2[0].close()

    # Receive results in main process
    try:
        while True:
            print(pipe_2[1].recv())
    except EOFError:
        print("End of Processing")

    p1.join()
    p2.join()
