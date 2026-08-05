class Queue:
    def __init__(self, queue):
        self.queue = queue
        
    def enqueue (self,element):
        self.queue.append(element)
        return self.queue

    def peek (self) :
        return self.queue[0]

    def isEmpty (self) :
        return len(self.queue) == 0

    def size (self) :
        return len(self.queue)

    def dequeue(self) :
        dequeing = Queue.peek(self)
        self.queue.pop(dequeing)
        return self.queue

class Node :
    def __init__ (self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

class BinaryTree :
    def __init__(self):
        self.root = None

    def check_fullness(node):
        full = 0
        if node.left_child != None:
            full += 1
        else:
            return 0
        if node.right_child != None:
            full += 1
        else:
            return 1
        if full == 2:
            return -1

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left_child)
        print(node.data)
        self.in_order(node.right_child)

    def pre_order(self, node):
        if node is None:
            return
        print(node.data)
        self.pre_order(node.left_child)
        self.pre_order(node.right_child)

    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left_child)
        self.post_order(node.right_child)
        print(node.data)

    def level_order(self, node):
        if node is None:
            return
        
        result = []
        queue = Queue([node])

        while not queue.isEmpty:
            current = queue.dequeue()
            result.append(current)

            if current.left_child is not None:
                queue.enqueue(current.left_child)

            if current.right_child is not None:
                queue.enqueue(current.right_child)

        return result
