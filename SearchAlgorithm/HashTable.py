class HashTable:
    def __init__(self):
        self.size = 10  # 假设散列表大小为 10
        self.table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if not self.table[index]:
            self.table[index] = []
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index]:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None
