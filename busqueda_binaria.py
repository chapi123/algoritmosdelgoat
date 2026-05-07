import random
import time
import matplotlib.pyplot as plt

def binary_search(nums, wanted):
    left = 0                        #1 operacion
    right = len(nums) - 1           #1 operacion
    
    while left <= right:            #loop que se ejecuta log n veces
        mid = (left + right) // 2   #1 operacion, log n veces
        
        if nums[mid] == wanted:     #1 operacion logica, log n comparaciones
            return mid          
        elif nums[mid] < wanted:    #1 operacion logica, log n comparaciones
            left = mid + 1     
        else:
            right = mid - 1    
    
    return -1                       #total de operaciones = 2 + 3*log n, O(log n)

sizes = [100, 1000, 10000, 100000, 500000, 1000000]
times = []

for size in sizes:
    nums = list(range(size))
    wanted = int(random.randint(0, size - 1))

    start = time.perf_counter()
    binary_search(nums, wanted)
    end = time.perf_counter()

    times.append(end - start)
    print(f"time for {size} numbers: {end - start:} seconds")

plt.plot(sizes, times, marker='o')
plt.xlabel("Number of Elements")
plt.ylabel("Time (seconds)")
plt.title("Binary Search Performance - O(log n)")
plt.grid(True)
plt.show()

#el grafico puede salir con una curva rara, pero eso depende del random,
#si se busca el peor caso siempre la linea va a ser mas recta