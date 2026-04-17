# Exercise:

#  Problem: Create a program that concurrently computes the factorial of several numbers using multi-processing.
#  Steps to Solve:
#   Define a recursive factorial function.
#   Spawn a process for each number in a list.

import multiprocessing
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def compute_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        start = time.perf_counter()
        logging.info(f"Computing factorial of {n} started. Process ID: {multiprocessing.current_process().pid}")
        p = multiprocessing.Process(target=compute_factorial, args=(n - 1,))
        p.start()
        p.join()
        end = time.perf_counter()
        logging.info(f"Computing factorial of {n} finished. Process ID: {multiprocessing.current_process().pid}. Time taken: {end - start:.6f} seconds")
        return n * compute_factorial(n - 1)


if __name__ == "__main__":
    result = compute_factorial(5)
    print(f"Factorial of 5 is: {result}")