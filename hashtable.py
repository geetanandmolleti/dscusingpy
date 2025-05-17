class SimpleHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Empty slots

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        if self.table[index] and self.table[index][0] == key:
            return self.table[index][1]
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] and self.table[index][0] == key:
            self.table[index] = None

    def display(self):
        for i, item in enumerate(self.table):
            print(f"{i}: {item}")

# Usage
ht = SimpleHashTable(5)
ht.insert("Ironman", "Tony Stark")
ht.insert("Thor", "God of Thunder")
ht.insert("Hulk", "Bruce Banner")

ht.display()
print("Get Hulk:", ht.get("Hulk"))

ht.delete("Thor")
ht.display()
