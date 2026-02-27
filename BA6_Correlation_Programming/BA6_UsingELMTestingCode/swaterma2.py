def smith_waterman2(seq1, seq2, match_score=2, mismatch_penalty=1, gap_penalty=1):
    n, m = len(seq1), len(seq2)
    # Initialize the scoring matrix
    score_matrix = [[0] * (m + 1) for _ in range(n + 1)]

    # Track the maximum score and the matrix position of this score
    max_score = 0
    max_pos = (0, 0)

    # Fill the score matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                score_diagonal = score_matrix[i - 1][j - 1] + match_score
            else:
                score_diagonal = score_matrix[i - 1][j - 1] - mismatch_penalty

            score_up = score_matrix[i - 1][j] - gap_penalty
            score_left = score_matrix[i][j - 1] - gap_penalty
            score_matrix[i][j] = max(0, score_diagonal, score_up, score_left)

            # Check if we have a new maximum score
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_pos = (i, j)

    # Trace back the highest scoring path
    aligned_seq1 = []
    aligned_seq2 = []
    i, j = max_pos

    while i > 0 and j > 0 and score_matrix[i][j] > 0:
        current_score = score_matrix[i][j]
        diagonal_score = score_matrix[i - 1][j - 1]
        up_score = score_matrix[i - 1][j]
        left_score = score_matrix[i][j - 1]

        if current_score == diagonal_score + (match_score if seq1[i - 1] == seq2[j - 1] else -mismatch_penalty):
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif current_score == left_score - gap_penalty:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j - 1])
            j -= 1
        elif current_score == up_score - gap_penalty:
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append('-')
            i -= 1

    return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2)), max_score


# Example use of the function:
#seq1 = "GACTTAC"
#seq2 = "CGTGAATTCAT"
#aligned_seq1, aligned_seq2, alignment_score = smith_waterman2(seq1, seq2)

#print("Aligned Seq1:", aligned_seq1)
#print("Aligned Seq2:", aligned_seq2)
#print("Alignment Score:", alignment_score)
