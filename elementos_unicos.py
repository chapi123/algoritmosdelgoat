import random
import time
import matplotlib.pyplot as plt

times = []

def unique_elements(nums):
    for i in range(len(nums)):             #se ejecuta n veces
        for x in range(i + 1, len(nums)):  #se ejecuta n*(n-1)/2 veces
            if nums[i] == nums[x]:         #1 operacion logica
                return False               #1 operacion logica, solo si encuentra un elemento repetido
    return True                            #total de operaciones: n*(n-1)/2 → O(n²)                                       

sizes = [100, 500, 1000, 2000, 5000] 
times = []

for size in sizes:
    nums = list(range(size))  

    start = time.time()
    unique_elements(nums)
    end = time.time()

    times.append(end - start)
    print(f"time for {size} numbers: {end - start} seconds")

plt.plot(sizes, times, marker='o')
plt.xlabel("Number of Elements")
plt.ylabel("Time (seconds)")
plt.title("Unique Elements - O(n²)")
plt.grid(True)
plt.show()

#total de operaciones: n*(n-1)/2 → O(n²)
#se puede mejorar¿¿ si, usando un set, O(n), pero no es brute 

#el grafico puede salir con una curva rara, pero eso depende del random,
#si se busca el peor caso siempre la linea va a ser mas recta