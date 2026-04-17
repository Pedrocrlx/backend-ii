import multiprocessing
import threading

print(multiprocessing.cpu_count())
print(multiprocessing.current_process().name)
print(threading.current_thread().name)
print(threading.active_count())
