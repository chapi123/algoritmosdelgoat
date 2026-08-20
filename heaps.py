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

    def remove_at_location(self, index):
        try:
            removed = self.heap[index]
            self.heap.remove(index)
            self.size -= 1
            self.arrange()
            return removed            
        except:
            return False
        

    def delete_at_root(self):
        if self.size == 0:
            return None

        root = self.heap[1]

        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1

        if self.size > 0:
            self.sink_bottom()

        return root

    def sink_bottom(self):
        current = 1

        while True:
            child = self.min_child(current)

            if child is None:
                break

            if self.heap[current] > self.heap[child]:
                self.heap[current], self.heap[child] = (
                    self.heap[child],
                    self.heap[current]
                )
                current = child
            else:
                break

    def min_child(self, current):
        left = current * 2
        right = left + 1

        if left > self.size:
            return None

        if right > self.size:
            return left

        if self.heap[left] < self.heap[right]:
            return left
        else:
            return right

    def sort(self):
        sorted_list = []

        while self.size > 0:
            sorted_list.append(self.delete_at_root())

        return sorted_list