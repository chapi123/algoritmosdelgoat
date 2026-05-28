#queue
queue = [1,2,3]

def enqueue (element):
    queue.append(element)
    return queue

def peek () :
    return queue[0]

def isEmpty () :
    return len(queue) == 0

def size () :
    return len(queue)

def dequeue() :
    dequeing = peek()
    queue.pop(dequeing)
    return queue

print("----Queue----")
print(enqueue(6))
print(enqueue(7))
print(peek())
print(isEmpty())
print(size())
print(dequeue())
print("")

#stacks
stack = []

def push(element) :
    stack.append(element)
    return stack

def pop() :
    return stack.pop(-1)

def peek():
    return stack[len(stack)-1]

def isEmpty ():
    return len(stack) == 0

def size ():
    return len(stack)

print("----Stack----")
print(isEmpty())
print(push(2))
print(push(4))
print(pop())
print(stack)
print(size())
print(peek())