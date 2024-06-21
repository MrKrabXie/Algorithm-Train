import unittest

from SearchAlgorithm.HashTable import HashTable


# 假设散列查找的实现代码保存在 hash_search.py 中

class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.hash_table = HashTable()
        self.hash_table.insert("John", 25)
        self.hash_table.insert("Jane", 30)
        self.hash_table.insert("Doe", 35)

    def test_search_existing_key(self):
        self.assertEqual(self.hash_table.search("John"), 25)
        self.assertEqual(self.hash_table.search("Jane"), 30)
        self.assertEqual(self.hash_table.search("Doe"), 35)

    def test_search_non_existing_key(self):
        self.assertIsNone(self.hash_table.search("Smith"))

    def test_search_empty_table(self):
        empty_table = HashTable()
        self.assertIsNone(empty_table.search("John"))

if __name__ == "__main__":
    unittest.main()
