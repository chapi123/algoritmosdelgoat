from queue_stack_class import Stack

def surviving_fish(A,B):
    instance = Stack()
    survivors = 0

    for i in range(len(A)):
        
        if B[i] == 1:
            instance.push(A[i])

        else:
            
            while instance.peek() is not None and A[i] > instance.peek():
                instance.pop()

            if instance.isEmpty():
                survivors +=1
    
    return survivors + instance.size()

print(surviving_fish([2,5,7,9,2,4], [0,1,0,1,0,0]))