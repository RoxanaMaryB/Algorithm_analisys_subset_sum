import time
import tracemalloc

def measure_time_and_memory(func, *args, **kwargs):
    tracemalloc.start()  # Start tracing memory allocations
    start_time = time.perf_counter()  # Start time measurement with higher resolution
    result = func(*args, **kwargs)  # Run the function
    end_time = time.perf_counter()  # End time measurement with higher resolution
    execution_time = end_time - start_time  # Time taken by the function
    current, peak = tracemalloc.get_traced_memory()  # Get current and peak memory usage
    tracemalloc.stop()  # Stop tracing memory allocations

    memory_used = peak / (1024 * 1024)  # Convert bytes to MiB

    return result, execution_time, memory_used