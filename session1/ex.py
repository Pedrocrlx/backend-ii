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

logging.basicConfig(filename="./logs/factorial.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def factorial(n: int, count=0) -> tuple:
    count += 1
    logger.info(f"Factorial ({n}) called {count}")
    if n == 0:
        return 1, count    
    result, count = factorial  (n - 1, count)
    return n * result, count

start = time.perf_counter()
result, total_calls = factorial(10)
end = time.perf_counter()

print(f"factorial(10) = {result}")
print(f"Total recursive calls: {total_calls}")
print(f"Total execution time: {end - start:.6f}s")