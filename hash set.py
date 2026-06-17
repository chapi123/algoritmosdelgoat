from linked_list import SingleLink

def hash(a) :
    total = 0
    for i in str(a):
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
                x = self.hash(i)
                self.values_hashed.append(x)

        if values_hashed:
            self.values_hashed = values_hashed

        self.buckets = [SingleLink() for _ in range(self.size)]
        for i in self.values_hashed:
            index = self.get_index(i, self.size)
            self.buckets[index].add_node()
        for bucket in self.buckets:
            print(bucket.count_nodes())

    def hash(a) :
        total = 0
        for i in str(a):
            total += ord(i)
        return total
    
    def get_index (self, key, n):
        return key % n
    
    def add_value (self, data):
        data_hashed = self.hash(data)

        if self.get_item(data):
            return False


        index = self.get_index(data_hashed, self.size)
        self.buckets[index].add_node(data)
        return True
    
    def print_values(self):
        for bucket in self.buckets:
            bucket.print_values()

    def remove(self, data):
            data_hashed = self.hash(data)
            index = self.get_item(data_hashed, self.size)

            return self.buckets[index].delete(data_hashed)
    
    def get_item(self, data):
            data_hashed = self.hash(data)
            index = self.get_index(data_hashed, self.size)

            return self.buckets[index].get_item(data_hashed)

class Bucket_probing:
    def __init__(self, size, values=None, values_hashed=None):
        self.size = size

        if values:
            self.values_hashed = []
            for i in values:
                x = self.hash(i)
                self.values_hashed.append(x)

        if values_hashed:
            self.values_hashed = values_hashed
    
    def get_index (self, key, n):
        return key % n
    
    def hash(a) :
        total = 0
        for i in str(a):
            total += ord(i)
        return total

    def main(self):
        bucket = [None for _ in range(self.size)]

        for i in self.values_hashed:
            inserted = False
            index = self.get_index(i, self.size)
            attempts = 0

            while not inserted and attempts < self.size:
                if bucket[index] is None:
                    bucket[index] = i
                    inserted = True
                else:
                    index = (index + 1) % self.size
                    attempts += 1

            if not inserted:
                raise Exception("full hash table")
            