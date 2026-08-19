class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        self.arrange()

    def arrange(self):
        current = self.size
        while current // 2:
            if self.heap[current] <= self.heap[current // 2]:
                self.heap[current], self.heap[current // 2] = self.heap[current // 2], self.heap[current]
            current //= 2
                


    def sons(self, index):
        left_son = index * 2
        right_son = index * 2 + 1
        try: 
            left_son = self.heap[left_son]
        except:
            left_son = None
        try: 
            right_son = self.heap[right_son]
        except:
            right_son = None
        return left_son, right_son

    def show(self, index):
        return self.heap[index]

    def delete(self, data):
        self.heap.remove(data)
        self.size -= 1
        self.arrange()

    def delete_at_root(self)
