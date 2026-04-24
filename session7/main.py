## Write complexty function for try time.perf_counter() decorator
from util import time_perf


@time_perf
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(150))
