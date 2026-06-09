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

    def add_node(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def count_nodes(self):
        current = self.head
        nodes = 0
        while current is not None:
            current = current.next
            nodes += 1
        return nodes

    def sort_nodes(self):
        changed = True
        while changed:
            current = self.head
            changed = False
            while current is not None and current.next is not None:
                if current.data > current.next.data :
                    current.data, current.next.data = current.next.data, current.data
                    changed = True         
                current = current.next
    
    def invert_nodes(self):
        nodes = self.count_nodes()

        for i in range(nodes//2):
            left = self.get_item(i)
            right = self.get_item(nodes-1-i)

            left.data, right.data = right.data, left.data


instance = SingleLink([1,2,3,4,5,7,8])
instance.invert_nodes()
instance.print_values()


class DoubleLink:
    def __init__ (self, values):
        
        nodes = [Node(value) for value in values]

        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        for i  in range(len(nodes)):
            if i == 0: pass
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
    
class CircularSingleLink:
    def __init__ (self, values):
        
        nodes = [Node(value) for value in values]

        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        self.head = nodes[0]
        self.tail = nodes[-1]

        self.tail.next = self.head

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

class CircularDoublyList:
    def __init__ (self, values):
        
        nodes = [Node(value) for value in values]

        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        for i  in range(len(nodes)):
            if i == 0: pass
            else:
                nodes[i].prev = nodes[i-1]

        self.head = nodes[0]
        self.tail = nodes[-1]

        self.tail.next = self.head
        self.head.prev = self.tail

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
        