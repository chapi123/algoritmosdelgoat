from queue_stack_class import Stack

def nest (nest) :
    instance = Stack('')
    for i in nest:
        if i in '[({' :
            Stack.push(instance,i)

        if i == '(':
            if i == Stack.peek(instance) or Stack.isEmpty(instance):
                return 0
            Stack.pop(instance)

        if i == '[':
            if i == Stack.peek(instance) or Stack.isEmpty(instance):
                return 0
            Stack.pop()

        if i == '{':
            if i == Stack.peek(instance) or Stack.isEmpty(instance):
                return 0
            Stack.pop(instance) 
    
    if Stack.isEmpty(instance):
        return 1
    else:
        return 0
    
nest('[()]')