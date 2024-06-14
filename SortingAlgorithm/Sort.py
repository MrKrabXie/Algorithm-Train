import time
import unittest
from memory_profiler import profile


"""
 import random
    
    # 生成几百万个随机数作为测试数据集生成不同的序列， 每个
    random_sequences = random.sample(range(1000000), 10000)
    
  # 使用装饰器来监控函数的执行时间， profile是空间的注解， 因为我们关注时间和空间所以这里啊都加上了  
    
"""
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


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

class TestBubbleSort(unittest.TestCase):
    # 使用装饰器来监控函数的执行时间， profile是空间的注解， 因为我们关注时间和空间所以这里啊都加上了
    @performance_monitor
    @profile
    def test_bubble_sort(self):
        # arr = [64, 34, 25, 12, 22, 11, 90]

        # 在这里调用排序算法并进行模拟

        bubble_sort(random_sequences)
        # n = len(random_sequences)
        # for i in range(n):
        #     for j in range(0, n-i-1):
        #         if random_sequences[j] > random_sequences[j+1]:
        #             random_sequences[j], random_sequences[j+1] = random_sequences[j+1], random_sequences[j]
        # sorted_arr = [11, 12, 22, 25, 34, 64, 90]
        # self.assertEqual(arr, sorted_arr)



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

class TestInsertionSort(unittest.TestCase):

    def test_insertion_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        insertion_sort(arr)
        sorted_arr = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(arr, sorted_arr)


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

class TestSelectionSort(unittest.TestCase):

    def test_selection_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        selection_sort(arr)
        sorted_arr = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(arr, sorted_arr)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

class TestQuickSort(unittest.TestCase):

    def test_quick_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = quick_sort(arr)
        expected_arr = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(sorted_arr, expected_arr)

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

class TestShellSort(unittest.TestCase):

    def test_shell_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        shell_sort(arr)
        sorted_arr = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(arr, sorted_arr)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

class TestHeapSort(unittest.TestCase):

    def test_heap_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        heap_sort(arr)
        sorted_arr = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(arr, sorted_arr)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        merge_sort(arr)
        sorted_arr = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(arr, sorted_arr)

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

class TestRadixSort(unittest.TestCase):

    def test_radix_sort(self):
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        radix_sort(arr)
        sorted_arr = [2, 24, 45, 66, 75, 90, 170, 802]
        self.assertEqual(arr, sorted_arr)

if __name__ == '__main__':
    unittest.main()
