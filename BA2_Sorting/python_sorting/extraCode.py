import time # a library needed fo timing functions
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import the scripts
from bubbleSort import bubbleSort
from quickSort import quickSortS
from selectionSort import selectionSort


#This reads a file...
def readFile(fle):
    f = open(fle, 'r')
    x = f.readlines()
    f.close()
    results = [int(i) for i in x]
    return results


#This can be passed a file to sort and the sort algorithm
def testPerformance(filename,algorithm):
    arr2 = readFile(filename)
    start = time.time()
    algorithm(arr2)
    elapsed =time.time()-start

    #how to print the elapsed time
    print("")
    print("Sorted big container: %s secs" % elapsed)
    for i in range(10):
           print(arr2[i],end=" ")
    print("")
    return elapsed 

#driver code example
file_list = ["random5000.txt", "random20000.txt", "random5000sorted.txt"]
alg_dict = {"bubblesort": bubbleSort, "quicksort": quickSortS, "selectionsort": selectionSort}
t_series = []
alg_series = []
file_series = []

for file in file_list:
    for alg, func in alg_dict.items():
        print(f"\nSorting using \"{alg}\" and \"{file}\"")
        t = testPerformance(file, func)
        t_series.append(t)
        alg_series.append(alg)
        file_series.append(file)

df = pd.DataFrame({"Algorithm": pd.Series(alg_series), "File": pd.Series(file_series), "Time": pd.Series(t_series)})

alg_uniq = sorted(df["Algorithm"].unique().tolist())
fig1 = plt.figure(figsize = (15, 12))

for i, alg in enumerate(alg_uniq):
     temp = df[df["Algorithm"] == alg_uniq[i]]
     count = i + 1
     ax = fig1.add_subplot(len(alg_uniq), 1, count)
     sns.barplot(x = "File", y = "Time", data = temp)

fig1.tight_layout()
plt.savefig(f"exectime.png")

# print("\nSorting using \"bubbleSort\" and \"random5000.txt\"")
# bubble_5000_time = testPerformance("random5000.txt", bubbleSort)
# print("\nSorting using \"quickSortS\" and \"random5000.txt\"")
# quick_5000_time = testPerformance("random5000.txt", quickSortS)
# print("\nSorting using \"selsctionSort\" and \"random5000.txt\"")
# select_5000_time = testPerformance("random5000.txt", selectionSort)
# print("\nSorting using \"bubbleSort\" and \"random20000.txt\"")
# bubble_20000_time = testPerformance("random20000.txt", bubbleSort)
# print("\nSorting using \"quickSortS\" and \"random20000.txt\"")
# quick_20000_time = testPerformance("random20000.txt", quickSortS)
# print("\nSorting using \"selsctionSort\" and \"random20000.txt\"")
# select_20000_time = testPerformance("random20000.txt", selectionSort)

