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

    def iscycled (self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False

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
        prev = None
        current = self.head
        self.tail = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

instance = SingleLink([1,2,3,5,6,8,5,5,7,9,4,2,4,7,69,67])
instance.tail.next = instance.get_item(3)
print(instance.iscycled())

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
        