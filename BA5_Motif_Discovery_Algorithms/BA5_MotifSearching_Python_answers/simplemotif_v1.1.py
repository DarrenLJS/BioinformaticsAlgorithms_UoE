# In this example we load two example files
# "Oct4.pos.fasta" contains sequence enriched from ChIP-seq experiment (peak centres) using Oct4
# "bground.fasta" contains the background (non-enriched) sequences from the same experiment
# This code reads these files and searches for enrichment using Python dictionaries
# Complete the analysis and output the results of sorted 8bp enriched sequences
# Note we use 8bp because Oct4 is an "Octamer binding protein", it is known to bind 8mers
# The most common known binding site for Oct4 is ATCGCAAAT
#Data processed from Chen, X., Xu, H., Yuan, P., Fang, F., Huss, M., Vega, V. B.,Wong, E., Orlov, Y. L., Zhang, W., Jiang, J. et al. (2008b).
# Integration of external signaling pathways with the core transcriptional network in embryonic stem cells. Cell 133,1106-1117.
#Simon Tomlinson Bioinformatics Algorithms Teaching Code 2025

from operator import itemgetter
import re
import time #for simple timing of the routines

def normaliseDict(mydict):
    # count total reads
    # express as percent total

    count = 0

    for myseq in mydict.keys():
        count = count + mydict[myseq]
    count = count / 100

    for myseq in mydict.keys():
        mydict[myseq] = mydict[myseq] / count


def processSeq(mydict, myline, kmer):
    # go though the line chopping sequence
    p = re.compile('[^ATGC]', re.IGNORECASE)
	#see https://pythonforbiologists.com/tutorial/regex.html
	#This matches any character not in ATGC

    for i in range(0, len(myline) - kmer):
        # do something
        myword = myline[i:i + kmer] # eg start 1 end before 1+8=9 so indexes 1,2,3,4,5,6,7,8 [the 8mer we want]

        # we ignore issues of case here
        if myword.find("N") != -1:
            continue
        if len(myword) != kmer:
            continue
        if p.match(myword):
            continue

        # print(myword)

        if myword not in mydict:
            mydict[myword] = 1 #We've found it so add the 1
        else:
            mydict[myword] += 1 #We've found more so increase by 1


def buildDictionary(fastafile, kmer):

#This is a very simple FSM-Finite State Machine
#Note how we progress from reading the body =True to False
#As we move through the file

    f1 = open(fastafile, 'r')
    f1lines = f1.readlines()
    readBody = False
    myline = ""
    mydict = {}

    for line in f1lines:
        line = line.rstrip()
        if line.startswith('>'):
            if readBody == True:
                # we are ending the processing of a seq
                processSeq(mydict, myline, kmer)
                readBody = False

        if readBody == False:
            myline = ""
            readBody = True
        else:
            if len(line) > 0:
                myline = myline + line
    f1.close()

    if (readBody == True):
        processSeq(mydict, myline, kmer)

    return mydict


def compareDictionaries(kmer):
    t1 = time.time()
    print("Building Dictionaries... with Kmer size=",kmer)

    # just load the two files and count each kmer
    print("Building Foreground")
    dictforeground = buildDictionary("Oct4.pos.fasta", kmer)
    print("Building Background")
    dictbackground = buildDictionary("bground.fasta", kmer)

    print("Normalising & Writing Dictionaries...")
    # normalise by size
    normaliseDict(dictforeground)
    normaliseDict(dictbackground)
    F = open("testfile_fg.txt", "w") #We open it for writing and then output data
    for myseq in sorted(dictforeground.items(), key=itemgetter(1), reverse=True):  #We use itemfgetter to get the element of the dict to sort on - key or count here
        #  print(myseq[0])
        if (len(myseq[0]) != kmer):
            continue
        F.write(myseq[0])
        F.write("\t")
        F.write(str(myseq[-1]))
        F.write("\n")
    F.close()

    F = open("testfile_bg.txt", "w")
    for myseq in sorted(dictbackground.items(), key=itemgetter(1), reverse=True):
        #  print(myseq[0])
        if (len(myseq[0]) != kmer):
            continue
        F.write(myseq[0])
        F.write("\t")
        F.write(str(myseq[-1]))
        F.write("\n")
    F.close()

#combined
    print("Writing Combined Files...")
    dictcombined={}
    for myseq in sorted(dictforeground.items(), key=itemgetter(1), reverse=True):
        #  print(myseq[0])
        if (len(myseq[0]) != kmer):
            continue
        #check the background
        background =dictbackground.get(myseq[0],1)#1 heee is used when n seq of this type in bg
        dictcombined[myseq[0]]=myseq[1]-background

    F = open("testfile_combined.txt", "w")
    for myseq in sorted(dictcombined.items(), key=itemgetter(1), reverse=True):
        #  print(myseq[0])
        F.write(myseq[0])
        F.write("\t")
        F.write(str(myseq[-1]))
        F.write("\n")
    F.close()
    t2 = time.time()
    print("All Completed...in ",t2-t1," secs")
# actually run the programme
compareDictionaries(8)
