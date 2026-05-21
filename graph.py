import random
import time
import matplotlib.pyplot as plt

def graph(sizes, names, *args):
    graphs = len(args)
    
    if len(names) != graphs:
        raise ValueError("The number of labels does not match the number of time lists.")

    for i in range(graphs):
        times = args[i]
        name = names[i]

        plt.plot(sizes, times, marker='o', label=name)

    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithm Performance")
    plt.grid(True)
    plt.legend()
    plt.show()
