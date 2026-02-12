# Simon Tomlinson Bioinformatics Algorithms
# Perform Smith Waterman Alignment in Python (from first principles)
# contains rows lists each of length cols initially set to 0
# index as my_matrix[1][2] my_matrix[R][C]
# Teaching code!!
#Version 1.9 SRT

from SmithWaterman_questions import read_fasta_filename
import argparse

parser = argparse.ArgumentParser(description='Aligning sequences...')
parser.add_argument('seq1',action="store",help="First sequence")
parser.add_argument('seq2',action="store",help="Second sequence")

args = parser.parse_args()

if args.seq1.endswith(".fasta"):
    sequence1 = read_fasta_filename(args.seq1)
if args.seq2.endswith(".fasta"):
    sequence2 = read_fasta_filename(args.seq2)
else:
    sequence1 = args.seq1
    sequence2 = args.seq2

from enum import Enum

#Global enumeration used for tracement
TypeB = Enum('TypeB', ['INSERT', 'DELETE', 'MISMATCH', 'MATCH', 'END'])


def create_matrix(rows, cols):
    my_matrix = [[0 for col in range(cols + 1)] for row in range(rows + 1)]
    return my_matrix


# x is row index, y is column index
# follows[r][c]

def calc_score(matrix, x, y):
    # print("seq1:",sequence1[y- 1]," seq2: "+sequence2[x - 1],"x:",x," y:",y)

    sc = seqmatch if sequence1[y - 1] == sequence2[x - 1] else seqmismatch

    base_score = matrix[x - 1][y - 1] + sc
    insert_score = matrix[x - 1][y] + seqgap
    delete_score = matrix[x][y - 1] + seqgap
    v = max(0, base_score, insert_score, delete_score)
    return v


# makes a single traceback step
def traceback(mymatrix, maxv):
    x = maxv[0]
    y = maxv[-1]
    val = mymatrix[x][y]

    # todo add some outputs for checking errors
    sc = seqmatch if sequence2[x - 1] == sequence1[y - 1] else seqmismatch
    base_score = mymatrix[x - 1][y - 1] + sc
    if base_score == val:
        if sc==seqmatch:
            return [x - 1,TypeB.MATCH, y - 1]
        else:
            return [x - 1,TypeB.MISMATCH, y - 1]

    insert_score = mymatrix[x - 1][y] + seqgap
    if insert_score == val:
        return [x - 1, TypeB.INSERT, y]
    else:
        return [x, TypeB.DELETE, y - 1]


# builds the initial scoring matrix used for traceback
def build_matrix(mymatrix):
    rows = len(mymatrix)
    cols = len(mymatrix[0])

    for i in range(1, rows):
        for j in range(1, cols):
            mymatrix[i][j] = calc_score(mymatrix, i, j)

    return mymatrix


# gets the max value from the built matrix
# Max is the end of the traceback for SW
def get_max(mymatrix):
    max = mymatrix[0][0]
    mrow = 0
    mcol = 0

    rows = len(mymatrix)
    cols = len(mymatrix[0])

    for i in range(1, rows):
        for j in range(1, cols):
            if mymatrix[i][j] > max:
                max = mymatrix[i][j]
                mrow = i
                mcol = j
    print("max score: ", max)
    return [mrow, TypeB.END, mcol]


# print out the best scoring path from the SW matrix
def print_matrix(mymatrix):
    rows = len(mymatrix)
    cols = len(mymatrix[0])
    s1 = "  " + sequence1
    s2 = " " + sequence2

    print("Dimensions: r= %2d , c= %2d" % (rows, cols))

    for a in s1:
        print(a, end="")
        print(" \t", end="")
    print("\n", end="")

    for i in range(0, rows):
        print(s2[i], end="")
        print(" \t", end="")
        for j in range(0, cols):
            print("%02d\t" % (mymatrix[i][j]), end="")
        print("\n", end="")


# print out the traceback of the best scoring alignment
def print_traceback(mymatrix):
    # this will print as expected with internal gaps
    print("Building traceback...")
    maxv = get_max(mymatrix)

    #stash the max score for later
    max_score = mymatrix[maxv[0]][maxv[-1]]

    # traverse the matrix to find the traceback elements
    # if more than one path just pick one
    topstring = ""
    midstring = ""
    bottomstring = ""

    # pad the sequences so indexes into the sequences match the matrix indexes
    asequence1 = "#" + sequence1
    asequence2 = "#" + sequence2

    #this vector is used to store the traceback results

    traversal_results = []

    # add the rest of the elements
    search = True
    lastelement = False

    while (search):

        #debug print("position: %d, %s, %d" % (maxv[0], maxv[1], maxv[-1]))
        #store the results
        traversal_results.append(maxv)

        maxv = traceback(mymatrix, maxv)


        #catch the trivial case that we are at the end of one of the sequences
        if (maxv[-1] < 0 or maxv[0] < 0):
            traversal_results.append(maxv)
            search= False
            continue


        if (mymatrix[maxv[0]][maxv[-1]] == 0 and lastelement == False):
            lastelement = True
            continue

        if(lastelement==True) :
            search= False
            traversal_results.append(maxv)
            continue


    for i in range(0, len(traversal_results)-2):

        #The TypeB of the next element gives how the current element was reached
        #in the dynamic programming table
        #The current element gives the index of the two matching bases to be aligned

        curr_el=traversal_results[i]
        next_el=traversal_results[i+1]

        #Match
        if(next_el[1]==TypeB.MATCH):
            bottomstring += asequence2[curr_el[0]]
            topstring += asequence1[curr_el[-1]]
            midstring +="|"

        #Mismatch
        elif(next_el[1]==TypeB.MISMATCH):
            bottomstring += asequence2[curr_el[0]]
            topstring += asequence1[curr_el[-1]]
            midstring += "."

        elif(next_el[1]==TypeB.INSERT):
            bottomstring += asequence2[curr_el[0]]
            topstring += "-"
            midstring += " "

        elif(next_el[1]==TypeB.DELETE):
            bottomstring += "-"
            topstring += asequence1[curr_el[-1]]
            midstring += " "

    print("\nFinal Alignment, Score: %d" % max_score)

    print(topstring[::-1])
    print(midstring[::-1])
    print(bottomstring[::-1])

# build the SW alignment...
def perform_smith_waterman():
    # values for weights
    global seqmatch
    global seqmismatch
    global seqgap
    global sequence1
    global sequence2

    # note these are not the exact weights used in the original SW paper
    seqmatch = 1
    seqmismatch = -1
    seqgap = -1

    # input sequences- other examples
    #sequence1="AGTGATAAACTAGTAATTTTT"
    #sequence2="TTGGGGGTAAACAGGGG"

  #  sequence1 ="AGTCGGTTAGTAAA"
  #  sequence2 ="TTTTGGGTTTAGGCGC"

 #   sequence1 = "GTGTATTTTTTT"
 #   sequence2 = "AAAAGTGTTATT"

 #   sequence1 = "TCGTTCTAG"
 #   sequence2 = "TCGTTTTTG"

 #   sequence1 = "SimonTomkinson"
 #   sequence2 = "SimonTomlinsonBioinformaticsAlgorithms"

    print("Sequence1: " + sequence1)
    print("Sequence2: " + sequence2)

    mymatrix = create_matrix(len(sequence2), len(sequence1))
    mymatrix = build_matrix(mymatrix)
    print_matrix(mymatrix)

    print_traceback(mymatrix)


##this calls the SW algorithm when the script loads
perform_smith_waterman()
