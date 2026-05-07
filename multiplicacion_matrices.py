import random
import time
import matplotlib.pyplot as plt

def matrix_multiply(A, B, n):
    result = [[0] * n for _ in range(n)]  #crea matriz n×n llena de ceros, n operaciones
    
    for i in range(n):          #loop externo, recorre filas → n veces
        for j in range(n):      #loop medio, recorre columnas → n veces por cada i → n² veces total
            for k in range(n):  #hace la suma → n veces por cada i,j → n³ veces total
                result[i][j] += A[i][k] * B[k][j]  # 2 operaciones (multiplicacion + suma) → 2*n³ en total
    
    return result                       #total de operaciones: n + 2*n³ → O(n³)



sizes = [10, 50, 100, 200, 300] 
times = []

for size in sizes:
    A = [[random.randint(0, 10) for _ in range(size)] for _ in range(size)]
    B = [[random.randint(0, 10) for _ in range(size)] for _ in range(size)]

    start = time.time()
    matrix_multiply(A, B, size)
    end = time.time()

    times.append(end - start)
    print(f"time for {size}x{size} matrix: {end - start:.6f} seconds")

plt.plot(sizes, times, marker='o')
plt.xlabel("Matrix Dimension (n)")
plt.ylabel("Time (seconds)")
plt.title("Matrix Multiplication - O(n³)")
plt.grid(True)
plt.show()

#se puede mejorar¿ si, existe el algoritmo de Strassen que lo reduce a O(n^2.8),
#lo encontre buscando con ia, pero es complicado de implementar

#el grafico puede salir con una curva rara, pero eso depende del random,
#si se busca el peor caso siempre la linea va a ser mas recta