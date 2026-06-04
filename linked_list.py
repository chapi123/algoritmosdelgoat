class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SingleLink:
    def __init__ (self, values):
        
        nodes = [Node(value) for value in values]

        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        self.head = nodes[0]
        self.tail = nodes[-1]


    def print_values (self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    def iscicled (self):
        return self.tail == None

    def get_item (self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current


instance = SingleLink([1,2,4,6,8,0,4])
print(instance[1].data)