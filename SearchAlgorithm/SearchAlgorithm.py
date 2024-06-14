import time
import unittest

def performance_monitor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} executed in {execution_time} seconds")
        return result
    return wrapper

import random

# 生成几百万个随机数作为测试数据集生成不同的序列， 每个
random_sequences = random.sample(range(1000000), 10000)


if __name__ == '__main__':
    unittest.main()
