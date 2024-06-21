def find_max(nums):
    """
    Finds the maximum value in a list of numbers.

    Args:
    - nums: A list of numbers.

    Returns:
    - The maximum value in the list.
    """
    if not nums:
        return None

    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num

    return max_value
import unittest

class TestFindMax(unittest.TestCase):

    def test_find_max_basic(self):
        # Test case with positive numbers
        nums = [1, 3, 5, 2, 4]
        self.assertEqual(find_max(nums), 5)

    def test_find_max_negative(self):
        # Test case with negative numbers
        nums = [-1, -3, -5, -2, -4]
        self.assertEqual(find_max(nums), -1)

    def test_find_max_mixed(self):
        # Test case with mixed positive and negative numbers
        nums = [-1, 3, -5, 2, 0]
        self.assertEqual(find_max(nums), 3)

    def test_find_max_single_element(self):
        # Test case with a single element
        nums = [3]
        self.assertEqual(find_max(nums), 3)

    def test_find_max_empty_list(self):
        # Test case with an empty list
        nums = []
        self.assertIsNone(find_max(nums))

    def test_find_max_duplicates(self):
        # Test case with duplicate values
        nums = [5, 5, 5, 5, 5]
        self.assertEqual(find_max(nums), 5)

if __name__ == '__main__':
    unittest.main()
