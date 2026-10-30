def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    row_l = len(a)
    col_l = len(a[0])
    r = []

    for j in range(col_l):
        temp = []
        for i in range(row_l):
            temp.append(a[i][j])
        r.append(temp)

    return r


