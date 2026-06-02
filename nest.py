from queue_stack_class import Stack

def nest(text):
    stack = Stack()

    for c in text:

        if c in "([{":
            stack.push(c)

        elif c == ")":
            if stack.isEmpty() or stack.peek() != "(":
                return 0
            stack.pop()

        elif c == "]":
            if stack.isEmpty() or stack.peek() != "[":
                return 0
            stack.pop()

        elif c == "}":
            if stack.isEmpty() or stack.peek() != "{":
                return 0
            stack.pop()

    return 1 if stack.isEmpty() else 0

print(nest('[())]'))