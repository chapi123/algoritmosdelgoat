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
        return current.data

class DoubleLink:
    
    def __init__ (self, values):
        
        nodes = [Node(value) for value in values]

        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        
        for i in range(len(nodes)):
            if i == 0 : pass
            else:
                nodes[i].prev = nodes[i-1]

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


instance = DoubleLink([1,2,5,7,8,9])
print(instance.get_item(4).prev.data)