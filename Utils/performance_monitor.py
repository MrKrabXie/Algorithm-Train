# performance_monitor.py
import time

class PerformanceMonitor:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {self.func.__name__} executed in {execution_time} seconds")
        return result
