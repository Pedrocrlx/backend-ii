## This file contains tests for multiprocessing in Python,
#  Demonstrating various approaches to parallel execution and inter-process communication.

import multiprocessing
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(processName)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def compute_square(n):
    time.sleep(0.5)
    return n * n


def compute_cube(n):
    time.sleep(0.5)
    return n * n * n


def worker_with_result(queue, n, operation):
    result = operation(n)
    queue.put((n, result))
    logger.info(f"Processed {n} -> {result}")


def test_basic_process():
    logger.info("=== Test: Basic Process ===")
    start = time.perf_counter()

    p = multiprocessing.Process(target=compute_square, args=(5,))
    p.start()
    p.join()

    end = time.perf_counter()
    logger.info(f"Basic process took: {end - start:.2f}s")
    return end - start


def test_multiple_processes():
    logger.info("=== Test: Multiple Processes ===")
    numbers = [1, 2, 3, 4, 5]
    start = time.perf_counter()

    processes = []
    for n in numbers:
        p = multiprocessing.Process(target=compute_square, args=(n,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.perf_counter()
    logger.info(f"Multiple processes took: {end - start:.2f}s")
    return end - start


def test_process_pool():
    logger.info("=== Test: Process Pool ===")
    numbers = [1, 2, 3, 4, 5]
    start = time.perf_counter()

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(compute_square, numbers)

    end = time.perf_counter()
    logger.info(f"Pool results: {results}")
    logger.info(f"Process pool took: {end - start:.2f}s")
    return end - start


def test_process_pool_with_different_operations():
    logger.info("=== Test: Pool with Different Operations ===")
    numbers = [1, 2, 3, 4, 5]
    start = time.perf_counter()

    with multiprocessing.Pool(processes=4) as pool:
        squares = pool.map(compute_square, numbers)
        cubes = pool.map(compute_cube, numbers)

    end = time.perf_counter()
    logger.info(f"Squares: {squares}")
    logger.info(f"Cubes: {cubes}")
    logger.info(f"Pool with different ops took: {end - start:.2f}s")
    return end - start


def test_shared_queue():
    logger.info("=== Test: Shared Queue ===")
    numbers = [1, 2, 3, 4, 5]
    queue = multiprocessing.Queue()
    start = time.perf_counter()

    processes = []
    for n in numbers:
        p = multiprocessing.Process(
            target=worker_with_result, args=(queue, n, compute_square)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    results = []
    while not queue.empty():
        results.append(queue.get())

    end = time.perf_counter()
    logger.info(f"Queue results: {results}")
    logger.info(f"Shared queue took: {end - start:.2f}s")
    return end - start


def test_sequential():
    logger.info("=== Test: Sequential (Baseline) ===")
    numbers = [1, 2, 3, 4, 5]
    start = time.perf_counter()

    results = [compute_square(n) for n in numbers]

    end = time.perf_counter()
    logger.info(f"Sequential results: {results}")
    logger.info(f"Sequential took: {end - start:.2f}s")
    return end - start


if __name__ == "__main__":
    logger.info(f"CPU count: {multiprocessing.cpu_count()}")
    logger.info("Starting multiprocessing tests...\n")

    seq_time = test_sequential()
    basic_time = test_basic_process()
    multi_time = test_multiple_processes()
    pool_time = test_process_pool()
    pool_ops_time = test_process_pool_with_different_operations()
    queue_time = test_shared_queue()

    logger.info("\n=== Summary ===")
    logger.info(f"Sequential:        {seq_time:.2f}s")
    logger.info(f"Basic Process:    {basic_time:.2f}s")
    logger.info(f"Multiple Procs:   {multi_time:.2f}s")
    logger.info(f"Process Pool:     {pool_time:.2f}s")
    logger.info(f"Pool + Ops:       {pool_ops_time:.2f}s")
    logger.info(f"Shared Queue:     {queue_time:.2f}s")
