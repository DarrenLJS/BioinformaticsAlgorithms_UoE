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

#Version 1.9 SRT


#Q1: Indexing Strings
testsequence="AGCGATDTTT"
print("Original:", testsequence)
#Q1a: How do you obtain the third character of testsequence and print it to screen?
print("Second character:", testsequence[2])
#Q1B: How do you return the second and third characters?
print("Second and third characters:", testsequence[1:3])
#Q1C: How do you change the last character of "testsequence" to an "A" using Python code?
newsequence = testsequence[:-1] + "A"
print("Replacing last character with 'A':", newsequence)
#Q1D: What value does testsequence[-1] equal?
print("testsequence[-1] = Last character:", testsequence[-1])
#Q1E: Will "testsequence[len(testsequence)]" (without quotes)  generate an error?  If so why?
print(
    """
    f"testsequence[len(testsequence)] will not generate an error, 
    as it accesses the last character/index of testsequence {testsequence[len(testsequence)]}.
    """
)

#Q2 Change counters
x=1
x+1
print(x) 

#Q2A: What is the value of x printed?  Why?
print(f"x = {x} as global variable x does not change.")
#Q3: Define Functions

y=1
def myfunction(aval):
    aval=4
    return (y+1)

#Q3A: Call this function with "myfunction(y)", what is the value of y after this call
print(f"myfunction(y) = {myfunction(y)} as myfunction returns (y+1) which calls global variable y = 1")
#Q3B: What is the value of "aval" after the call to myfunction ??
print("aval = 4")

#Q4: Passing and returning values
#Q4A Define a function that is passed  an integer and returns this integer incremented by one
def inc_one(someint):
     return someint+1

#Q5: Assignment and equivalence
z=4
if(z==True):
    print(z)
#Will "z" print in this code?
print("z:", z)

#Q6: Simple loops
count=0
for i in range(1, 10):
         for j in range(1, 2):
             count=count+1

#What is the value of count?
print("count loop:", count)

#Q7: Parse a file
#Modify the code below to write a function that reads a fasta file
#and returns the sequence, ignoring the header
#"afile" and "bfile" are 

#Use Biopython for real projects that read fasta!!!
def read_fasta_filename(filename):
   seq=""

   with open(filename, 'r') as filehandle:
       for line in filehandle:
           print(line)
           if not line.startswith(">"):
                seq = line
       return seq

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


#Q9: Load the SmithWaterman.py code and run the aligner.
#Read the code and determine how to change the input parameters including the files to be aligned.
#Change the code to align a different set of sequences.  
#Does the aligner give consistent results to the water programme online?


#Q10: SmithWaterman.py Code Questions
#Q10A: Read the code of SmithWaterman.py and identify how the matrix is initialised, where is the recurrence relationship defined?
print("Initialise a matrix of 0s of len(sequence2) x len(sequence1)")
#Q10B: What does the "range" command specify?
print("range(from, to, step) specifies a list of numbers")
#Q10C:
#In the line 41 "sc = seqmatch if sequence2[x - 1] == sequence1[y - 1] else seqmismatch" why are indexes x and y offset by -1?
#Q10D: Why "mymatrix[0]" in the code from line 510  "cols=len(mymatrix[0])"?
#Q10E: What does the command at line 85 do  "return [mrow, TypeB.END, mcol]"?
#Q10F: Line 100 "print("\n",end="")" what does "\n" specify?
#Q10G: Line 106 "print("%02d\t" % (mymatrix[i][j]),end="")" what does the "%" specify?
#Q10H: Line 203 "global  seqmatch" why "global"?
#Q10I Could you remove the call to  "perform_smith_waterman()", line 200, and still run the code?








