import re
#This class uses the Smith Waterman Algorithm as an example of how to implement an algorithm in Python.
#In this  class we review key Python features and then modify an existing Smith-Waterman implementation
#This is expected to be a refresher for most people and we do not cover all commands used in the code

#But you don't need much knowledge of Python here- we use small subset of the language

#You need to understand, indexing strings, counters, defining fuctions, passing  and returning values from functions
#You need to understand assignment and equivalence
#You need to understand simple loop structures
#In this example we index a Python list and treat it like an array, we make a list of list and this is a matrix
#We will explore other ways to define a matrix-like data structure in a later classes
#For the exercises you need to know how to read and parse a file

#Version 2.0 SRT


#Q1: Indexing Strings
testsequence="AGCGATDTTT"

# Q1a: How do you obtain the third character of testsequence and print it to screen?
print("third: ",testsequence[2])
# Q1B: How do you return the second and third characters?
print("second_third ", testsequence[1:3])
# Q1C: How do you change the last character of "testsequence" to an "A" using Python code?
print("before edit: ", testsequence)
testsequence2 =testsequence[0:len(testsequence)-1]+"A"
print("after edit:", testsequence2)
#Note: strings are immutable in Python

# Q1D: What value does testsequence[-1] equal?
print("the last character of ",testsequence, " is ", testsequence[-1])

# Q1E: Will "testsequence[len(testsequence)]" (without quotes)  generate an error?  If so why?
#Yes out of bounds index - testsequence[len(testsequence)]

#Q2 Change counters
x=1
x+1
print(x) 

#Q2A: What is the value of x printed?  Why?
#We might have expected 2 but this is not becuase we have not assigned the result
x = x+1
print("Q2A, value of x ", x)


#Q3: Define Functions

y=1
def myfunction(aval):
    aval=4
    return (y+1)

#Q3A: Call this function with "myfunction(y)", what is the value of y after this call
print("Q3a myfunction ",myfunction(y))
print("Q3a myfunction av ",y)

#The passed value is assigned 4 but the result of this assignment is not returned from the function
#The value of y from the callee scope is visible within the function and this is incremented and returned

#Q3B: What is the value of "aval" after the call to myfunction ??
#print("aval after call ", aval)
#aval is not defined- it is in function scope and only exists while the function is running!



#Q4: Passing and returning values
#Q4A Define a function that is passed  an integer and returns this integer incremented by one
def myincrement(aval):
    return (aval + 1)

print("increment 1 by 1 =",myincrement(1))


#Q5: Assignment and equivalence
z=4
if(z==True):
    print(z)
#Will "z" print in this code?
#No! This is quite confusing- in most languages a numeric z value would evaluate to True if z>0, false if z==0

#Q6: Simple loops
count=0
for i in range(1, 10):
         for j in range(1, 2):
             count=count+1

#What is the value of count?
#Obviously try to work this out from the code before computationally!
#The point is that ranges in range(1,10) are between 1 and 10- they include 1 but not 10
print("Q6 count: ",count)


#Q7: Parse a file
#Modify the code below to write a function that reads a fasta file
#and returns the sequence, ignoring the header
#"afile" and "bfile" are 

#Use Biopython or similar for real projects that read fasta!!!
def read_fasta_filename(filename):
   seq=""

   with open(filename, 'r') as filehandle:
       for line in filehandle:
           print(line)
       return

#Answer...	   
def read_fasta_filename(filename):
    seq = ""

    with open(filename, 'r') as filehandle:

        for line in filehandle:

            if(line[0]== ">"):
                continue
            #OK but better to use a regular expression re.search(pattern, line):
            #eg re.search("^>",line)
            #We need to really search for ">" as the first character- there may be whitespaces!!

            print(line)
        return	   
	   
#call function with example file
#read_fasta_filename("afile.fasta")

#Q8: Command line
#Below is a code example of how to parse the command line using argparse.  
#Modify this code so that you can pick up the settings for SmithWaterman.py as parameter passed to the application
#Build a modified SmithWaterman.py Python programme

#import argparse

#parser = argparse.ArgumentParser(description='Aligning sequences...')
#parser.add_argument('seq1',action="store",help="First sequence")
#parser.add_argument('seq2',action="store",help="Second sequence")
#parser.add_argument('anum',action="store",help="A number",type =int)

#args = parser.parse_args()
#print(args)
#print(args.seq1)


#Q8 Answer
#An answer to this question is provided in another file


#Q9: Load the SmithWaterman.py code and run the aligner.
#Read the code and determine how to change the input parameters including the files to be aligned.
#Change the code to align a different set of sequences.  
#Does the aligner give consistent results to the water programme online?

#Parameters are mostly set in the "def perform_smith_waterman()" function
#Water should give the same results for DNA sequences- you have to set the gap penalties to match and also the distance matrix.
#When there are multiple equally scoring paths the programmes might pick different examples- but they should all have the same score!


#Q10: SmithWaterman.py Code Questions
#Q10A: Read the code of SmithWaterman.py and identify how the matrix is initialised, where is the recurrence relationship defined?

#build_matrix(mymatrix) inits the matrix
#calc_score(matrix, x, y) for recurrence but also to some extent in the traceback (TODO use one encoding of this relationship and call for both)


#Q10B: What does the "range" command specify?
#This sets a range of values to be iterated, first value starts, second value is one past the end-

#Q10C:
#In the line 41 "sc = seqmatch if sequence2[x - 1] == sequence1[y - 1] else seqmismatch" why are indexes x and y offset by -1?
#This refers to the actual character index of the sequences
#Indexes are -1 offset compared to the matrix indexes because the matrix has an extra row and column compared to the sequence to accomodate gaps


#Q10D: Why "mymatrix[0]" in the code from line 510  "cols=len(mymatrix[0])"?
#Just the index of the forst column- setting the row and column parameters here that are used later in the code.


#Q10E: What does the command at line 85 do  "return [mrow, TypeB.END, mcol]"?
#This is a Tuple (sort of like a fixed list) that is used to represent a position used for traceback so a row column co-ordinate
#The Enum value (something more often seen in the C/C++ programming languages, just is something that can be one of a set of values
#Here it is set to define the end of the sequence.

#Q10F: Line 100 "print("\n",end="")" what does "\n" specify?
#This just specifies a newline character.  However this is for Unix (although Windows/Mac often used this as well.
#To write code that works on any platform it is better to use os.linesep (see later)

#Q10G: Line 106 "print("%02d\t" % (mymatrix[i][j]),end="")" what does the "%" specify?
#Here we feed the variable (mymatrix[i][j]) into the string "%02d\t" % links the string with the variable


#Q10H: Line 203 "global  seqmatch" why "global"?
#This tells the function look for the variable seqmatch as a global rather than declared within the function.


#Q10I Could you remove the call to  "perform_smith_waterman()", line 200, and still run the code?
#Yes you could just then import the file into another file and call the function from the importing script (for example) 







