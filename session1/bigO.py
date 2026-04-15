## Example -----------------------


# def linear_search(lst, target):
#     for item in lst:
#         if item == target:
#             return True
#     return False


# print(linear_search([4, 10, 5], 10))

## Exercise -----------------------
import logging
import time

logger = logging.getLogger(__name__)

def recursive(n: int, count=0) -> tuple:
    logging.basicConfig(filename="./recursive.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    if n == 1:
        return 1, count
    count += 1
    start = time.perf_counter()
    logger.info(f"Started, exec time: {start}")
    result, count = recursive(n - 1, count)
    end = time.perf_counter()
    logger.info(f"Finish, exec time: {end}")
    return n * result, count

print(recursive(10))
