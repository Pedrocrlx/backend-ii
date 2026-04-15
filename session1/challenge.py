## Session 1 Challenge with Binary Search instead of Bubble Sort

numbers = [1, 2, 3, 4, 5, 6]
import logging
import timeit

logger = logging.getLogger(__name__)


def binary_search(list: list):
    logging.basicConfig(filename="./challenge.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    start = timeit.timeit()
    logger.info(f"Started, exec time: {start}")
    ordered_list = sorted(list)
    mid = (ordered_list[0] + ordered_list[-1]) / 2
    end = timeit.timeit()
    logger.info(f"Finished, exec time: {end}")
    return print(f"Mid: {mid}")


binary_search(numbers)
