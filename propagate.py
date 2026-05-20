#0 (nuevo), un 1 (encendido) o un -1 (carbonizado)

def propagate(vector):
    changed = True

    while changed:
        changed = False

        for i in range(len(vector)):

            if vector[i] == 1:

                if i > 0 and vector[i-1] == 0:
                    vector[i-1] = 1
                    changed = True

                if i < len(vector)-1 and vector[i+1] == 0:
                    vector[i+1] = 1
                    changed = True

    return vector

print(propagate([0,0,0,0,-1,0,0,0,1]))
