
#Called with parameters "AAAAA" "TTTTT"  46


#Build a modified SmithWaterman.py Python programme
import argparse

parser = argparse.ArgumentParser(description='Aligning sequences...')
parser.add_argument('seq1',action="store",help="First sequence")
parser.add_argument('seq2',action="store",help="Second sequence")
parser.add_argument('anum',action="store",help="A number",type =int)

args = parser.parse_args()
print(args)
print("This is the first parameter", args.seq1)
print("This is the second parameter", args.seq2)
print("This is the third parameter", args.anum)