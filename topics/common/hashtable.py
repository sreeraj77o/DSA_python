class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._hash(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                pair[1] = value  # Update existing key
                return
        self.buckets[index].append([key, value])
    
    def get(self, key):
        index = self._hash(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found
    
    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.buckets[index]):
            if pair[0] == key:
                self.buckets[index].pop(i)
                return

# Test the hash map
hm = HashMap()
hm.put("name", "Alice")
hm.put("age", 25)
print("Name:", hm.get("name"))  # Output: Name: Alice
print("Age:", hm.get("age"))    # Output: Age: 25
hm.remove("name")
print("Name after remove:", hm.get("name"))  # Output: Name after remove: None