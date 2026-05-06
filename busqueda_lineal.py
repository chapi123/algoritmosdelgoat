import random
import time
import matplotlib.pyplot as plt

def linear_search(nums, wanted):
    for i in nums:                  #se ejecuta n veces
        if i == wanted:             #1 operacion logica, n comparaciones 
            return nums.index(i)    #1 operacion, solo si lo encuentra
    return -1                       #total de operaciones = n + 1, O(n)

sizes = [100, 1000, 10000, 100000, 500000, 1000000]
times = []

for size in sizes:
    nums = list(range(size))
    wanted = int(random.randint(0, size - 1))

    start = time.time()
    linear_search(nums, wanted)
    end = time.time()

    times.append(end - start)
    print(f"time for {size} numbers: {end - start:} seconds")

plt.plot(sizes, times, marker='o')
plt.xlabel("Number of Elements")
plt.ylabel("Time (seconds)")
plt.title("Linear Search Performance - O(n)")
plt.grid(True)
plt.show()

#puede mejorarse¿¿ si, usando busqueda binaria pasa a O(log n),
#pero requiere que la lista esté ordenada

#el grafico puede salir con una curva rara, pero eso depende del random,
#si se busca el peor caso siempre la linea va a ser mas recta