import random
import time
import matplotlib.pyplot as plt

from graph import graph

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

def insertion_sort(listt):
    for i in range(1, len(listt)):
        value = listt[i]
        x = i - 1

        while x >= 0 and value < listt[x]:
            listt[x + 1] = listt[x]
            x -= 1

        listt[x + 1] = value

    return listt

def main () :
    sizes = [100, 1000, 5000, 10000]
    times_b = []
    times_s = []
    times_i = []

    for size in sizes:
        listt = [random.randint(1, size) for _ in range(size)]

        start = time.perf_counter()
        bubble_sort(listt.copy())
        times_b.append(time.perf_counter() - start)

        start = time.perf_counter()
        selection_sort(listt.copy())
        times_s.append(time.perf_counter() - start)

        start = time.perf_counter()
        insertion_sort(listt.copy())
        times_i.append(time.perf_counter() - start)

    names = ['Bubble Sort', 'Selection Sort', 'Insertion Sort']

    graph(sizes, names, times_b, times_s, times_i)

if __name__ == "__main__":
    main()