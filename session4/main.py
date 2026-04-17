import multiprocessing
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def compute_square(n):
    time.sleep(1)  # Simulate a heavy computation
    print(f"Square of {n} is {n*n}")
if __name__ == "__main__":
    # numbers = [2, 3, 4, 5]
    # processes = []
    # for number in numbers:
    #     p = multiprocessing.Process(target=compute_square, args=(number,))
    #     processes.append(p)
    #     p.start()
    # for p in processes:
    #     p.join()
    logging.info("Starting the computation...")
    start = time.perf_counter()
    p = multiprocessing.Process(target=compute_square, args=(2,))
    p.start()
    p.join()
    end = time.perf_counter()
    print(f"Time taken: {end - start}")
    logging.info("Finished the computation...")
