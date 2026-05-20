import random
import time
import matplotlib.pyplot as plt

def bubble_sort(listt):
    for i in range(len(listt)):
        for i in range(len(listt) - 1):

            x = listt[i]
            y = listt[i + 1]

            if x > y:
                listt[i], listt[i + 1] = listt[i + 1], listt[i]
    return listt

def selection_sort(listt):
    for i in range(len(listt)):
        min_index = i
        for x in range(i + 1, len(listt)):
            if listt[x] < listt[min_index]:
                min_index = x
        listt[i], listt[min_index] = listt[min_index], listt[i]
    return listt


def main () :
    sizes = [100, 1000, 5000, 10000]
    times_b = []
    times_s = []
    for size in sizes :
        listt = []
        
        for i in range(size):
            listt.append(random.randint(1,size))
        
        start = time.perf_counter()
        bubble_sort(listt.copy())
        end = time.perf_counter()
        times_b.append(end - start)
        print(f"time for {size} numbers with bubble sort: {end - start:} seconds")

        start = time.perf_counter()
        selection_sort(listt.copy())
        end = time.perf_counter()
        times_s.append(end - start)
        print(f"time for {size} numbers with selection sort: {end - start:} seconds")

    plt.plot(sizes, times_b, marker='o', label='Bubble Sort')
    plt.plot(sizes, times_s, marker='o', label='Selection Sort')

    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithm Performance")
    plt.grid(True)
    plt.legend()

    plt.show()



main()