import logging
import time


def time_perf(func):
    def wrapper(*args, **kwargs):
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            filename="app.log",
        )
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        logging.info(f"Function {func.__name__} took {end - start:.4f} seconds")
        return result

    return wrapper


@time_perf
def calculations(a):
    numbers = [i for i in range(a)]
    return print(numbers)


calculations(10000000)
