#This is a simple implementation of a MapReduce algorithm in Python
#The challenge is to make sense of the code!
#The code generates a long list of random sequences and then counts the most common sequence using MapReduce
#Work out how it does this and where each method fits into MapReduce -where are the Mappers and Reducers?
#Note that this is a very simple algorithm and we only need one Reducer why?
#Could we change the code to add more than one Reducer?
#Do you think the chunking- splitting the data into parts for running on the Mappers works in a reasonable way?  How might this
#be improved?
#Change the number of threads and the number of sequences and see how performance changes- is this what you'd expect?
#If you have time change the application to lead kmers from genomic sequence- what is the most common kmer sequence in
#the mouse genome?


import random
import string
import time
import timeit
from multiprocessing import Pool

#A Simply Map Reduce Application to find the most common sequence in a random set of sequence
def chunk_alist(data, chunk_size):
  listoflists=[]

  sze=int((len(data)-1)/(chunk_size))
  stopp=len(data)

  for i in range(0,stopp , sze):
      listoflists.append(list(data[i:i + sze]))
  return listoflists

#Generates random strings of length 4
def createRandomStrings(count, seqlen=2):

  mylist=[]

  for x in range(count):
       letters = "AG"
       str=''.join(random.choice(letters) for i in range(seqlen))
       mylist.append(str)
  return mylist

#Count the occurrence of each string using a dictionary
def getStringCounts(alist):
    strCounts={}

    for x in alist:
       if x in strCounts:
           strCounts[x]=strCounts.get(x)+1
       else:
           strCounts[x]=1

    return strCounts

#iterate key value pairs to find the seq with the highest count
def findMostFrequent(mappedv):
    fullset = {}

    for i in range(0, len(mappedv)):
              #fullset.update(mappedv[i])- add manually as merge does not seem to work
       mkeys=mappedv[i].keys()
       for x in mkeys:
                  if x in fullset:
                      fullset[x] = fullset.get(x) + mappedv[i].get(x)
                  else:
                      fullset[x] = mappedv[i].get(x)


    # get the key values
    mykeys=list(fullset.keys())

    bestkey =""
    bestvalue=0

    for ky in mykeys:
        if(fullset[ky]>bestvalue):
            bestvalue=fullset[ky]
            bestkey=ky

    return bestkey,bestvalue

#this finds the elements of interest
def runMapReduce(count,cores,seq_length=2):
  pool=Pool(cores)

 #first build some strings
  mystrings =createRandomStrings(count,seq_length)

  starttime = timeit.default_timer()

 #chop strings into N sets of elements
  mystrings_chunked =chunk_alist(mystrings, cores)
 #Analyse the chunks
  mappedv = pool.map(getStringCounts, mystrings_chunked)

 #Combine the results
  best=findMostFrequent(mappedv)

  endtime = timeit.default_timer()

#output final results
  print(mystrings_chunked)
  print("Best key: ",best[0]," Best value: ",best[-1], "in ",endtime-starttime, " seconds")

#This ensures the threads will work correctly with the main
if __name__ == '__main__':

  #this is runMapReduce(seq count,thread count, seq length)
   random.seed(time.time())
   runMapReduce(40,2,3)
