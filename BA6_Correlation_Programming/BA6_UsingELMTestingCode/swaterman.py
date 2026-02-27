#from ELM -https://elm.edina.ac.uk/elm/elm

def smith_waterman(seq1, seq2, match_score=2, mismatch_cost=1, gap_cost=1):
    # Initialize the scoring matrix
    n, m = len(seq1), len(seq2)
    score_matrix = [[0] * (m + 1) for _ in range(n + 1)]

    # Track the maximum score and the position of the maximum score
    max_score = 0
    max_pos = None

    # Fill in the scoring matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = score_matrix[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else -mismatch_cost)
            delete = score_matrix[i-1][j] - gap_cost
            insert = score_matrix[i][j-1] - gap_cost
            score = max(0, match, delete, insert)

            score_matrix[i][j] = score

            if score > max_score:
                max_score = score
                max_pos = (i, j)

    # Trace back from the highest scoring cell
    aligned_seq1, aligned_seq2 = [], []
    i, j = max_pos
    while score_matrix[i][j] > 0:
        score = score_matrix[i][j]
        diagonal_score = score_matrix[i-1][j-1]
        up_score = score_matrix[i-1][j]
        left_score = score_matrix[i][j-1]

        if score == diagonal_score + (match_score if seq1[i-1] == seq2[j-1] else -mismatch_cost):
            aligned_seq1.append(seq1[i-1])
            aligned_seq2.append(seq2[j-1])
            i -= 1
            j -= 1
        elif score == up_score - gap_cost:
            aligned_seq1.append(seq1[i-1])
            aligned_seq2.append('-')
            i -= 1
        else:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j-1])
            j -= 1

    # Since the traceback started at the max position, the sequences will be reversed
    return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2)), max_score

# Example use
#seq1 = "GACTTACGG"
#seq2 = "CGTGAATTCAT"
#aligned_seq1, aligned_seq2, alignment_score = smith_waterman(seq1, seq2)
#print("Aligned seq1:", aligned_seq1)
#print("Aligned seq2:", aligned_seq2)
#print("Alignment Score:", alignment_score)
