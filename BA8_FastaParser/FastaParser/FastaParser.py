import os
import re
#  Simple Fasta Import code. Do not use for general work!!
#  Use a well-tested parse implementations e.g. from BioPython!!!
#  Stores similarity matrix-used to ID valid alphabet
#  Simon Tomlinson  Bioinformatics  Algorithms 2024


class SimilarityMatrix:
    def __init__(self, filename):
        self.filename = filename

    #   Todo build the parse function
    def parse(self):

        return 0

    # debug
    def getalphabet(self):
        return "agctAGCT"


# stores a single record element of a fasta file
class FastaElement:
    def __init__(self, header, seq):
        self.header = header
        self.seq = seq

    def print(self):
        return self.header + "\n" + self.seq

    def __eq__(self, other):
        return self.header == other.header and self.seq == other.seq

    def isempty(self):
        return len(self.header) == 0 and len(self.seq == 0)

    def noheader(self):
        return len(self.header) == 0

    def noseq(self):
        return len(self.seq) == 0

    def toupper(self):
        return FastaElement(self.header.upper(), self.seq.upper())


class FastaParse:
    def __init__(self, filename):
        self.filename = filename

        self.fastatable = []
        self.linenumber = 0
        self.skipcount = 0
        self.error_lines = ""
        self.parsing_seq = False
        self.parsing_header = False

    def getseq_atindex(self, idx):
        if idx < 0 or idx >= len(self.fastatable):
            return ""
        return self.fastatable[idx].seq

    def getheader_atindex(self, idx):
        if idx < 0 or idx >= len(self.fastatable):
            return ""
        return self.fastatable[idx].header

    def sanitycheckparse(self):
        #   check there is a filename and has been a parse
        if len(self.filename) == 0:
            print("No Filename has been detected.. parse cannot have taken place")
            return -1

        if not os.path.isfile(self.filename):
            print("File does not exist")
            return -1

        print("Number of records found: %d" % len(self.fastatable))
        print("Number of lines found: %d" % self.linenumber)
        print("Number of non-blank lines skipped: %d" % self.skipcount)

        recordcount = 0
        mylinecount = 0

        with open(self.filename, 'r') as filehandle:

            for line in filehandle:
                mylinecount += 1
                if line[0] == ">":
                    recordcount += 1

        print("Number of records expected: %d" % recordcount)
        print("Number of lines found: %d" % mylinecount)

        if self.skipcount > 0:
            print("Warning: Some records lines have been skipped- please check input files")
            print("Processing can continue...")
            return 0
        if recordcount != len(self.fastatable) or self.linenumber != mylinecount:
            print("The number of lines or records is not as expected")
            return -1
        else:
            print("Record numbers and lines processed are as expected")
            return 0

    def parse(self, mysimmatrix):

        if not os.path.isfile(self.filename):
            error = "File: " + self.filename + " Does not exist!! Ending Parse"
            return error

        simmatrix = SimilarityMatrix(mysimmatrix)
    #   make sure container is empty
        self.fastatable.clear()

        self.tempheader = ""
        self.tempseq = ""

        parsing_seq = False
        parsing_header = False

        self.linenumber = 0
        self.skipcount = 0
        error_new = ""
        self.error_lines = ""

        print("Parsing..."+self.filename)

        with open(self.filename, 'r') as filehandle:

            for line in filehandle:
                self.linenumber += 1

                #   print out progress
                if self.linenumber % 10000 == 0:
                    print("#", end="")
                if self.linenumber % 400000 == 0:
                    print("")

                #   strip white spaces here
                line = line.strip()

                #   blank line
                if len(line) == 0:
                    continue

                #   found the header
                if line[0] == ">":
                    parsing_seq = False
                    parsing_header = True

                    #   store the previous sequence data - now have new header & record
                    if len(self.tempseq) > 0 and len(self.tempseq) > 0:
                        self.fastatable.append(FastaElement(self.tempheader, self.tempseq))
                    #   store the current header
                    self.tempheader = line[1:]
                    self.tempseq = ""

                #   might be a bad header line - check character set
                elif re.match("[^" + simmatrix.getalphabet() + "]", line) is not None:
                    parsing_seq = False
                    parsing_header = False

                    #    store some sort of error
                    self.error_new = "Bad header line:" + str(self.linenumber) + "\n"
                    self.error_new += line + "\n\n"
                    self.error_lines += self.error_new

                    self.tempheader = ""
                    self.tempseq = ""

                    self.skipcount += 1

                    continue
                #      first non-blank line after header
                elif parsing_header == True:
                    parsing_seq = True
                    parsing_header = False

                    self.tempseq += line
                #     later non-blank sequence lines after header
                elif parsing_header == False and parsing_seq == True:
                    self.tempseq += line.strip()
                else:
                    self.parsing_seq = False
                    self.parsing_header = False

                    self.tempheader = ""
                    self.tempseq = ""

                    self.skipcount += 1

            #   store the last record here as file does not end in > character!!
            self.fastatable.append(FastaElement(self.tempheader, self.tempseq))

            print("\nParse completed!\n")

            return self.error_lines

class FastParserTests:

    def __init__(self, temp_folder):

        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)

        self.temp_folder = temp_folder
        self.sim_location = "./datafiles/"
        self.sim_files = "EDNAFULL_srt"


        self.testfile1description = "Valid Fasta format DNA sequence"
        self.testfile2description = "Valid Fasta format with case,whitespace etc added"
        self.testfile3description = "Missing headers, bad characters and bad records"

        #   store the elements for the tests
        self.fastatable = []
        self.fastatable.append(FastaElement("seq1", "GATCTACTATCTATCTATC\nTTTTTTTTTTTTT"))
        self.fastatable.append(FastaElement("seq2", "GATCTACTATCTATCTATC"))
        self.fastatable.append(FastaElement("seq3", "GATCTACTATCTATCTATC"))
        self.fastatable.append(FastaElement("seq4", "GATCTACTATCTATCTATC"))
        self.fastatable.append(FastaElement("seq5", "GGGGGGGGTATC"))
        self.fastatable.append(FastaElement("seq6", "GATCTACTATCTATCTATC"))
        self.fastatable.append(FastaElement("seq7", "TTTTTTTG"))
        self.fastatable.append(FastaElement("seq8", "GATCTACTATCTATCTATC"))
        self.fastatable.append(FastaElement("seq9", "GATCTACTATCTATCTATC"))
        self.fastatable.append(FastaElement("seq10", "AAAAAAAAAAAAAAAAAAA"))
        #    block2
        self.fastatable.append(FastaElement("seq11", "GATCTACTATCTATCTATC\n\n"))
        self.fastatable.append(FastaElement("seq12", "GATCTACTATCTATCTATC"))
        self.fastatable.append(FastaElement("seq13", "GATCTACTATCTATCTATC\t"))
        self.fastatable.append(FastaElement("seq14", "GATCTACTATCTATCTATC"))
        self.fastatable.append(FastaElement("seq15", "GGGGGGGGTATC\n\n"))
        self.fastatable.append(FastaElement("seq16", "AAAAAAAAAAAAAAAAAAA\n\n\n\n\n"))
        self.fastatable.append(FastaElement("seq17", "tttttttG"))
        self.fastatable.append(FastaElement("seq18", "\tGATCTACTATCTATCTATC\t"))
        self.fastatable.append(FastaElement("seq19", "GATCTACTATCTATCTATC "))
        self.fastatable.append(FastaElement("seq20", "AAaaaaaaaaaaaaaaaAA"))
        #    block3
        self.fastatable.append(FastaElement("", "GATCTACTATCTATCTATC\n\n"))  #no header >
        self.fastatable.append(FastaElement("seq22", "TGATCTACTATCTATCTATC"))  #space " >"
        self.fastatable.append(FastaElement("seq23", "AAaaaaaaaaaaaaaaaAA\t"))
        self.fastatable.append(FastaElement("seq24", "GATCTACTATCTATCTATC"))
        self.fastatable.append(FastaElement("seq25", "GGGGGGGGTATC\n\n"))
        self.fastatable.append(FastaElement("seq26", "AAAAAAAAAAAAAAAAAAA\n\n\n\n\n"))
        self.fastatable.append(FastaElement("seq27", "tttttttG"))
        self.fastatable.append(FastaElement("seq28", "GATCTNNNNNNTCTATC"))
        self.fastatable.append(FastaElement("seq29", "GATCTACTATCTATCTATC "))
        self.fastatable.append(FastaElement("seq30", ""))

        # store the elements for the tests
        self.fastatable_result = []
        self.fastatable_result.append(FastaElement("seq1", "GATCTACTATCTATCTATCTTTTTTTTTTTTT"))
        self.fastatable_result.append(FastaElement("seq2", "GATCTACTATCTATCTATC"))
        self.fastatable_result.append(FastaElement("seq3", "GATCTACTATCTATCTATC"))
        self.fastatable_result.append(FastaElement("seq4", "GATCTACTATCTATCTATC"))
        self.fastatable_result.append(FastaElement("seq5", "GGGGGGGGTATC"))
        self.fastatable_result.append(FastaElement("seq6", "GATCTACTATCTATCTATC"))
        self.fastatable_result.append(FastaElement("seq7", "TTTTTTTG"))
        self.fastatable_result.append(FastaElement("seq8", "GATCTACTATCTATCTATC"))
        self.fastatable_result.append(FastaElement("seq9", "GATCTACTATCTATCTATC"))
        self.fastatable_result.append(FastaElement("seq10", "AAAAAAAAAAAAAAAAAAA"))
        # block2
        self.fastatable_result.append(FastaElement("seq11", "GATCTACTATCTATCTATC"))
        self.fastatable_result.append(FastaElement("seq12", "GATCTACTATCTATCTATC"))
        self.fastatable_result.append(FastaElement("seq13", "GATCTACTATCTATCTATC"))
        self.fastatable_result.append(FastaElement("seq14", "GATCTACTATCTATCTATC"))
        self.fastatable_result.append(FastaElement("seq15", "GGGGGGGGTATC"))
        self.fastatable_result.append(FastaElement("seq16", "AAAAAAAAAAAAAAAAAAA"))
        self.fastatable_result.append(FastaElement("seq17", "tttttttG"))
        self.fastatable_result.append(FastaElement("seq18", "GATCTACTATCTATCTATC"))
        self.fastatable_result.append(FastaElement("seq19", "GATCTACTATCTATCTATC"))
        self.fastatable_result.append(FastaElement("seq20", "AAaaaaaaaaaaaaaaaAA"))
        # block3

        self.fastatable_result.append(FastaElement("seq22", "TGATCTACTATCTATCTATC"))  # space " >" repair this issue
        self.fastatable_result.append(FastaElement("seq23", "AAaaaaaaaaaaaaaaaAA"))
        self.fastatable_result.append(FastaElement("seq24", "GATCTACTATCTATCTATC"))
        self.fastatable_result.append(FastaElement("seq25", "GGGGGGGGTATC"))
        self.fastatable_result.append(FastaElement("seq26", "AAAAAAAAAAAAAAAAAAA"))
        self.fastatable_result.append(FastaElement("seq27", "tttttttG"))
        self.fastatable_result.append(FastaElement("seq28", "GATCTNNNNNNTCTATC"))
        self.fastatable_result.append(FastaElement("seq29", "GATCTACTATCTATCTATC"))
        self.fastatable_result.append(FastaElement("seq30", ""))    #  delete this element

    def test(self):
        print("Testing parser using synthetic data...")

        if os.path.isdir(self.temp_folder) == False:
            print("Temp folder" + self.temp_folder + " does not exist")
            return -1

        fail_test1 = False
        fail_test2 = False
        fail_test3 = False

        #    dump out the testfiles
        self.write_testfile1()
        print("Testing load of standard data...")

        mySimMatrix = SimilarityMatrix(self.sim_location + self.sim_files)

        #   load some data
        parse1 = FastaParse(self.temp_folder + "/testfile1.fasta")

        parse1.parse(mySimMatrix)

        for x in range(0, 10):
            if parse1.fastatable[x].seq != self.fastatable_result[x].seq:
                print("Test failed: " + parse1.fastatable[x].seq + "!= expected "  + self.fastatable_result[x].seq)
                fail_test1 = True
                break

            elif parse1.fastatable[x].header != self.fastatable_result[x].header:
                print("Test failed: " + parse1.fastatable[x].header + " != expected " + self.fastatable_result[x].header)
                fail_test1 = True
                break
            else:
                print("Test sequence load: " + parse1.fastatable[x].header + " PASSED")

        self.write_testfile2()
        print("\nTesting load of slightly malformed  data...")

        # load some data
        parse2 = FastaParse(self.temp_folder + "/testfile2.fasta")

        parse2.parse(mySimMatrix)

        for x in range(0, 10):
            if parse2.fastatable[x].seq != self.fastatable_result[x+10].seq:
                print("Test failed: " + parse2.fastatable[x].seq + "!= expected " + self.fastatable_result[x+10].seq)
                fail_test2 = True
                break

            elif parse2.fastatable[x].header != self.fastatable_result[x+10].header:
                print("Test failed: " + parse2.fastatable[x].header + " != expected " + self.fastatable_result[x+10].header)
                fail_test2 = True
                break
            else:
                print("Test sequence load: " + parse2.fastatable[x].header + " PASSED")

        self.write_testfile3()
        print("\nTesting load of badly malformed  data with errors...")

        # load some data
        parse3 = FastaParse(self.temp_folder + "/testfile3.fasta")

        parse3.parse(mySimMatrix)

        for x in range(0, 9):
            if parse3.fastatable[x].seq != self.fastatable_result[x + 20].seq:
                print("Test failed: " + parse3.fastatable[x].seq + "!= expected " + self.fastatable_result[x + 20].seq)
                fail_test3 = True
                break

            elif parse3.fastatable[x].header != self.fastatable_result[x + 20].header:
                print("Test failed: " + parse3.fastatable[x].header + " != expected " + self.fastatable_result[x + 20].header)
                fail_test3 = True
                break
            else:
                print("Test sequence load: " + parse3.fastatable[x].header + " PASSED")

        if fail_test1 == False or fail_test2 == False or fail_test3 == False:
            return -1
        else:
            return 0

    def write_testfile1(self):

        filetowrite = self.temp_folder + "/testfile1.fasta"

        f = open(filetowrite, 'w')

        for x in range(0, 10):
            f.write(">" + self.fastatable[x].header + "\n")
            f.write(self.fastatable[x].seq + "\n")

        f.close()

    def write_testfile2(self):

        filetowrite = self.temp_folder + "/testfile2.fasta"

        f = open(filetowrite, 'w')

        for x in range(10, 20):
            f.write(">" + self.fastatable[x].header + "\n")
            f.write(self.fastatable[x].seq + "\n")

        f.close()

    def write_testfile3(self):

        filetowrite = self.temp_folder + "/testfile3.fasta"

        f = open(filetowrite, 'w')

        #   write non-standard test files
        f.write(self.fastatable[20].seq + "\n")

        f.write(" >" + self.fastatable[21].header + "\n")
        f.write(self.fastatable[21].seq + "\n")

        for x in range(22, 30):
            f.write(">" + self.fastatable[x].header + "\n")
            f.write(self.fastatable[x].seq + "\n")

        f.close()



fp = FastParserTests("tmp")
fp.test()