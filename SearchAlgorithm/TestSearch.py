
# Unit tests for linear_search function
import unittest

from SearchAlgorithm.SearchAlgorithm import *


class TestLinearSearch(unittest.TestCase):

    @PerformanceMonitor
    def test_found(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)

    @PerformanceMonitor
    def test_not_found(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 6), -1)

    @PerformanceMonitor
    def test_empty_list(self):
        self.assertEqual(linear_search([], 5), -1)

    @PerformanceMonitor
    def test_random_list(self):

        i = linear_search(random_sequences, 5000)
        print("返回索引为：" + i.__str__())


class TestBinarySearch(unittest.TestCase):

    def test_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([10, 20, 30, 40, 50], 40), 3)
        self.assertEqual(binary_search([5, 15, 25, 35, 45], 5), 0)
        self.assertEqual(binary_search([100], 100), 0)

    def test_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(binary_search([10, 20, 30, 40, 50], 35), -1)
        self.assertEqual(binary_search([5, 15, 25, 35, 45], 12), -1)
        self.assertEqual(binary_search([], 100), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 5), -1)

    @PerformanceMonitor
    def test_random_list(self):

        i = linear_search(random_sequences, 5000)
        print("返回索引为：" + i.__str__())

class TestInterpolationSearch(unittest.TestCase):

    def test_found(self):
        self.assertEqual(interpolation_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(interpolation_search([10, 20, 30, 40, 50], 40), 3)
        self.assertEqual(interpolation_search([5, 15, 25, 35, 45], 5), 0)
        self.assertEqual(interpolation_search([100], 100), 0)

    def test_not_found(self):
        self.assertEqual(interpolation_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(interpolation_search([10, 20, 30, 40, 50], 35), -1)
        self.assertEqual(interpolation_search([5, 15, 25, 35, 45], 12), -1)
        self.assertEqual(interpolation_search([], 100), -1)

    def test_empty_list(self):
        self.assertEqual(interpolation_search([], 5), -1)
