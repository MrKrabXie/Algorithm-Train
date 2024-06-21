import time
import unittest



import random

from Utils.performance_monitor import PerformanceMonitor

# 生成几百万个随机数作为测试数据集生成不同的序列， 每个
random_sequences = random.sample(range(1000000), 1000000)

def linear_search(arr, target):
    """
    Perform linear search to find the target value in the given list.

    Parameters:
    arr (list): The list in which to search.
    target: The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """
    Perform binary search to find the target value in the given sorted list.

    Parameters:
    arr (list): The sorted list in which to search.
    target: The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
def interpolation_search(arr, target):
    """
    Perform interpolation search to find the target value in the given sorted list.

    Parameters:
    arr (list): The sorted list in which to search.
    target: The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right and arr[left] <= target <= arr[right]:
        # Calculate the position with interpolation formula
        pos = left + (right - left) * (target - arr[left]) // (arr[right] - arr[left])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1

    return -1

def fibonacci_search(arr, target):
    """
    Perform Fibonacci search to find the target value in the given sorted list.

    Parameters:
    arr (list): The sorted list in which to search.
    target: The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    def fibonacci(n):
        fib = [0, 1]
        while fib[-1] < n:
            fib.append(fib[-1] + fib[-2])
        return fib

    n = len(arr)
    fib = fibonacci(n)
    k = len(fib) - 1

    while k > 1:
        idx = min(k - 1, n - 1)
        mid = fib[k - 1] - 1

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            k -= 1
            n = idx
        else:
            k -= 2

    return -1


if __name__ == '__main__':
    unittest.main()
