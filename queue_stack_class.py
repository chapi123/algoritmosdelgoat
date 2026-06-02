class Stack:
    def __init__(self, stack=None):
        if stack is None:
            self.stack = []
        elif isinstance(stack, str):
            self.stack = list(stack)
        else:
            self.stack = list(stack)

    def push(self, element):
        self.stack.append(element)
        return self.stack

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def transfer(self):
        newstack = []
        while not self.isEmpty():
            newstack.append(self.pop())
        return newstack

    def stacking_list(self):
        return [self.stack[-i - 1] for i in range(len(self.stack))]

    def empty(self):
        if self.isEmpty():
            return []
        self.pop()
        return self.empty()

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

def main ():
    c1 = Queue([1,2,3])
    print("----Queue----")
    print(Queue.enqueue(c1,6))
    print(Queue.enqueue(c1,7))
    print(Queue.peek(c1))
    print(Queue.isEmpty(c1))
    print(Queue.size(c1))
    print(Queue.dequeue(c1))
    print("")
    print("----Stack----")
    c2 = Stack([])
    print(Stack.isEmpty(c2))
    print(Stack.push(c2,2))
    print(Stack.push(c2,4))
    print(Stack.pop(c2))
    print(Stack.size(c2))
    print(Stack.peek(c2))
    print("")
    print("----Transfer----")
    c3 = Stack([3,5,7])
    print([3,5,7])
    print(Stack.transfer(c3))
    print("")
    print("----Recursive emptying----")
    print([3,5,7])
    print(Stack.empty(c3))
    print("")
    print("----List to stack----")
    print([3,4,7,3,7,8,0,1,2,5])
    c4 = Stack([3,4,7,3,7,8,0,1,2,5])
    print(Stack.stacking_list(c4))

if __name__ == '__main__':
    main()