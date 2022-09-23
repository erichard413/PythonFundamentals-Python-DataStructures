def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    count = 0
    idx = list(range(0,len(matrix)))
    rev_idx = list(range(0,len(matrix)))
    rev_idx.reverse()
    for num in idx:
        count += matrix[num][num]
        count += matrix[num][rev_idx[num]]
    return count