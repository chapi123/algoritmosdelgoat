from linked_list import SingleLink

def hash(a) :
    total = 0
    for i in a:
        total += ord(i)
    return total

def get_index_hash(key, n) :     # Este codigo recibe un valor para hashear y un valor n,
    return hash(key) % n    # se hace el modulo de base n del valor dado por el hash.

class Bucket_separate:
    def __init__(self, size, values=None, values_hashed=None):
        self.size = size

        if values:
            self.values_hashed = []
            for i in values:
                x = hash(i)
                self.values_hashed.append(x)

        if values_hashed:
            self.values_hashed = values_hashed
    
    def get_index (self, key, n):
        return key % n

    def main(self):
        buckets = [SingleLink() for _ in range(self.size)]
        for i in self.values_hashed:
            index = self.get_index(i, self.size)
            buckets[index].add_node(i)
        for bucket in buckets:
            print(bucket.count_nodes())

class Bucket_probing:
    def __init__(self, size, values=None, values_hashed=None):
        self.size = size

        if values:
            self.values_hashed = []
            for i in values:
                x = hash(i)
                self.values_hashed.append(x)

        if values_hashed:
            self.values_hashed = values_hashed
    
    def get_index (self, key, n):
        return key % n

    def main(self):
        bucket = []
