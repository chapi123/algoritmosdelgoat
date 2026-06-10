from linked_list import Node

class Stack:
    def __init__(self, values=None):
        if values:
            nodes = [Node(value) for value in values]

            for i in range(len(nodes)-1):
                nodes[i].next = nodes[i+1]

            self.head = nodes[0]
            self.tail = nodes[-1]
        else:
            self.head = None
            self.tail = None

    def push(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail= new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError("empty stack")

        value = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return value
    
    def peek(self):
        if self.head == None:
            return None
        return self.head.data
    
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        size = 0
        while current is not None:
            current = current.next
            size += 1
        return size

    def clean(self):
        if self.head == None:
            return True
        self.pop()
        return self.clean()
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None

        value = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return value

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        size = 0
        while current is not None:
            size += 1
            current = current.next
        return size
    
    def clean(self):
        if self.head == None:
            return True
        self.dequeue()
        return self.clean()