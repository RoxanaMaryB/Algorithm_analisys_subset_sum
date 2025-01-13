import time
import tracemalloc

def measure_time_and_memory(func, *args, **kwargs):
    tracemalloc.start()
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    memory_used = peak / (1024 * 1024)

    return result, execution_time, memory_used