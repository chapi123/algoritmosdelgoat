from linked_list import SingleLink

class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [SingleLink() for _ in range(size)]

    def hash(self, key):
        total = 0
        for char in str(key):
            total += ord(char)
        return total

    def get_index(self, key):
        return self.hash(key) % self.size

    def put(self, key, value):
        index = self.get_index(key)
        bucket = self.buckets[index]

        current = bucket.head

        while current is not None:
            if current.data[0] == key:
                current.data = (key, value)
                return
            current = current.next

        bucket.add_node((key, value))

    def get(self, key):
        index = self.get_index(key)
        bucket = self.buckets[index]

        current = bucket.head

        while current is not None:
            if current.data[0] == key:
                return current.data[1]
            current = current.next

        return None

    def remove(self, key):
        index = self.get_index(key)
        bucket = self.buckets[index]

        current = bucket.head

        while current is not None:
            if current.data[0] == key:
                return bucket.delete(current.data)
            current = current.next

        return False

    def print_map(self):
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}:")

            current = bucket.head

            while current is not None:
                key, value = current.data
                print(f"  {key}: {value}")
                current = current.next