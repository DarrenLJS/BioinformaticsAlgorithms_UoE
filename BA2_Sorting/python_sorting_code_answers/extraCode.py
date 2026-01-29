import time # a library needed fo timing functions

#import the scripts
from bubbleSort import bubbleSort
from quickSort import quickSortS
from selectionSort import selectionSort


#Tthis reads a file...
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
    print("Sorted array time: %s secs" % elapsed)
    for i in range(10):
           print(arr2[i],end=" ")
    return elapsed 



#use the  wrapper function to start quickSort
#You might also provide defauly parameters for the quickSort function
#def quickSortS(arr):
#    quickSort(arr,0,len(arr)-1)


#we can make code to exec in a big loop
myFunctions = [selectionSort,bubbleSort,quickSortS]
myFiles=["random5000.txt","random5000sorted.txt","random20000.txt"]
loops=3

for method in myFunctions:
    for fle in myFiles:
        for x in range (1, loops+1):

            #print out a descriptive header of the test performed
            print("")
            print("")
            print("Sorting using " + method.__name__,end="")
            print(" using filename " +"\"" + fle +"\"",end="")
            print(" %d of " % x,end="")
            print("%d loops " % loops)

            #do the actual test
            testPerformance(fle, method)