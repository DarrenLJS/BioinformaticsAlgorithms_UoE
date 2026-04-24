from operator import itemgetter
'''
The Python we have been using so far was defined in the Python Primer or in S1 Python programmming courses.  
In this class we review some of these features (with new examples) and then introduce a few extra
code features needed to understand the ICA.  The Blast code used in the ICA is
written using the basic features of Python introduced in the Python Primer, just with
a few extra extensions added along the way.  So here we review where we have got
so far with Python before extending to include these new features.  Of course, your
Python skills may extend beyond that set of skills from the Python Primer.  But
that's fine as long as the ICA code makes sense!!

Simon Tomlinson Bioinformatics Algorithms 2026
'''

#Q1 functions

def print_GATC():
    print("GATC")

#Call this function to print "GATC"

#Q2 functions- passing parameters
def print_bases(somebases):
    print(somebases)
#Change this function to enforce that the bases are GATC characters only

#Q3 functions
def reverse_complement_bases(somebases):
    replaceme = ""
    #your code here
#This time write a function to reverse complement the bases passed to the function

#Q4 Dictionaries associate keys with values and can then be look up these values
#This creates the dictionary
mymonth ={}

#This populates the dictionary with data
mymonth["Jan"] = 31
mymonth["Feb"] = 31
mymonth["Mar"] = 31
mymonth["Apr"] = 30
mymonth["May"] = 31
mymonth["Jun"] = 30
mymonth["Jul"] = 31
mymonth["Aug"] = 31
mymonth["Sep"] = 30
mymonth["Oct"] = 31
mymonth["Nov"] = 30
mymonth["Dec"] = 31

#Use this to find how many full days until the end of the current month?
#OK we ignore leap years here...

#Q5 tricky
def mydays(day, month, day2, month2):
    replaceme =""
    #Work out the number of days between day, month and day2, month2
    #By writing the code in raw Python- no cheating with libraries


#Q6 for loops can be used to iterate data
myseq ="GATGCGAAGCATGGGGGCTATAGCATAAAAAAAAAT"
#use a for loop to write out the sum of each base A, C, G and T

#Q7 ASCII coding
#ord() and chr() convert character to and from numbers
#We can use this as a simple checksum

test_sentence ="This is a test sentence for checksuming..."
#create a function that calculates the raw ASCII values of
#each character in this sentence and add these numbers together
#What value do you get?

#Q8 Tuples
#Tuples are a sort of immutable list- the elements cannot be changed
#Once created (without making a new copy of the object)

mytuple1 =(1,6,"test")
mytuple2 =(3,8,"test3")
mytuple3 =(2,1,"test2")
mytuple4 =(-1,2,"test4")

#make a list of these tuples
mytuples =[mytuple1,mytuple2,mytuple3,mytuple4]
#print the elements

#Q9 We can also sort the list using
#res.sort(key=itemgetter(2),reverse = True)
#itemgetter(2) gets the second index,3rd  element for sorting
#Sort the list by the first numerical column and print it out
#again

#Q10 Python has some useful operators for logical operations (or, and, is not etc)
x = 3
y = 4

if x < 4 or y<7:
    print("Found condition x <4 or y <7")

#We can also swap the conditions with functions
def print1():
    print("called print1")
    return True

def print2():
    print("called print2")
    return True

if print1() or print2():
    print("Finished...")

if print1() or print2():
    print("Finished...")

#Thats OK but the second function is not called if the first are true
#So we stop evaluation (moving left to right) when the first condition is true
#Since the functions print1 and print2 both return true print2 is never called
#How can we call both print1() and print2() but not print("Finished...")
#just by changing the operator


#Q11 functions can return more than one parameter
def functionret(var1,var2):
    return var1,var2
res1, res2 =functionret(1,2)
print("Res1: ", res1)
print("Res2: ", res2)
#change the example function to return a string and a short list

#Q12 Functions can have default values and named parameters
def functioneg(var1,var3=6,var12=7):
    print("My example: ",var1 + var3 + var12)
functioneg(1,2,3)
functioneg(3)

#Use default parameter to extend functions to add new parameters at the end of the parameter list
#This means that old calls to the function still work!

#Write a function that prints something passed to the function, but fails gracefully when the function is called
#without passing a string.

#Q13 A new Python print function variant - uses f-strings or formatted string
anumber =22/7
print(f"My number is {anumber}")

#Also quite good for rounding number to a given number of decimal places
print(f"My number is {anumber:.2f}")

#print out anumber as a percent using f-strings...


#Q14 Functions can call themselves
def gogo(p):
    if p <5 :
        print("Finally finished...at: ",p)
        return
    else:
        print("Still going...",p)
    gogo(p-1)

#call the function with a (small!) number
gogo(10)

#Write a function that converts a number from base 10 to base 2
#Either by having the function call itself or using a loop structure

#Q15
#You'll notice in the code that sometimes I use os.linesep as a newline character
#This is because Mac and Unix  use '\n' for a new line but windows uses '\r\n'
#Do you think this makes sense to do this if you want code to run on multiple platforms?