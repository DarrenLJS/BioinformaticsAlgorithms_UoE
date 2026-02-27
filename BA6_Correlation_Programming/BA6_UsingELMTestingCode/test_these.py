import swaterman as elm1
import swaterma2 as elm2
import SmithWaterman as SRT
import random


dict = "ACGT"

m_scores ="1234567"
mm_scores ="0123"
g_scores ="0123"

mat =0
mis = 0
gap = 0

#Set this to run the cycles
def regress_my_code(cycles =40):

    for i in range(0,cycles):
        len_seq1 =0
        len_seq2 =0

        while len_seq1 <10 or len_seq2 <10:
            len_seq1 = random.randrange(0,40)
            len_seq2 = random.randrange(0,40)

        print("len seq1:", len_seq1)
        print("len seq2:", len_seq2)

        seq1=[]
        seq2=[]
        for ii in range(0,len_seq1):
            seq1.append(random.choice(dict))
        for j in range(0, len_seq2):
            seq2.append(random.choice(dict))
        seq1 = ''.join(seq1)
        seq2 = ''.join(seq2)


        mat = int(random.choice(m_scores))
        mis = int(random.choice(mm_scores))
        gap = int(random.choice(g_scores))

        aligned_seq1, aligned_seq2, score1 = elm1.smith_waterman(seq1, seq2, mat, mis, gap)
        aligned_seq1, aligned_seq2, score2 = elm2.smith_waterman2(seq1, seq2,mat,mis,gap)
        score3 = SRT.perform_smith_waterman(seq1, seq2,mat,mis * -1,gap *-1)

        if  score2 !=score3 or score1 !=score2:

           print(" seq1: ",seq1)
           print(" seq2: ",seq2)
           print("score ELM: ", score1)
           print("score ELM2: ", score2)
           print("score SRT: ", score3)
           return 1
    print("completed: SUCCESSFULLY",i+1 ," trials")
    return 0

print("Check the code for this...")
regress_my_code(1000)