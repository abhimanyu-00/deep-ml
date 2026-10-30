def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
    if not a or not b:
        return -1

    if len(a[0]) != len(b):
        return -1

    row_l = len(a)
    col_l = len(b[0])
    common = len(a[0])
    c = []

    for i in range(row_l):
        temp = []
        for j in range(col_l):
            res = 0
            for k in range(common):
                res += a[i][k] * b[k][j]
            temp.append(res)

        c.append(temp)
    return c