import stack_queue_linked

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

    def inverse_polish_parser(self, expresion):
        caracters = expresion.split()
        Stack = stack_queue_linked.Stack()

        for i in caracters:
            if i in "+-/*":
                node = Node(i)
                node.right_child = Stack.pop()
                node.left_child = Stack.pop()
            else:
                node = Node(i)

            Stack.push(node)

        return Stack.pop()

    def evaluate(self, node):
        if node.data == "+":
            return self.evaluate(node.left_child) + self.evaluate(node.right_child)
        elif node.data == "-":
            return self.evaluate(node.left_child) - self.evaluate(node.right_child)
        elif node.data == "*":
            return self.evaluate(node.left_child) * self.evaluate(node.right_child)
        elif node.data == "/":
            return self.evaluate(node.left_child) / self.evaluate(node.right_child)
        else:
            return int(node.data)



    def calculate(self, node):
        if node.left_child is None and node.right_child is None:
            return int(node.data)

        left_child = self.calculate(node.left_child)
        right_child = self.calculate(node.right_child)

        if node.data == "+":
            return left_child + right_child
        elif node.data == "-":
            return left_child - right_child
        elif node.data == "*":
            return left_child * right_child
        elif node.data == "/":
            return left_child / right_child

NA = Node("A")
NB = Node("B")
NC = Node("C")
ND = Node("D")
NE = Node("E")
NF = Node("F")
NG = Node("G")

NA.left_child = NB
NA.right_child = NF
NB.left_child = NC
NB.right_child = NE
NF.left_child = NG
NC.left_child = ND

instance = BinaryTree()
instance.root = NA
instance.pre_order(NA)
instance.in_order(NA)
instance.post_order(NA)
instance.level_order(NA)
expression = "2 6 + 8 / 9 2 - *"
instance = BinaryTree()
root = instance.inverse_polish_parser(expression)
print(instance.evaluate(root))
print(instance.calculate(root))