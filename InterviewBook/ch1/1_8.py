import numpy as np


def ans_func(l_2d):
    m = len(l_2d)
    n = len(l_2d[0])

    zero_rows = set()
    zero_columns = set()
    for i in range(m):
        for j in range(n):
            if l_2d[i][j] == 0:
                zero_rows.add(i)
                zero_columns.add(j)
    for row in zero_rows:
        l_2d[row] = [0] * n
    for column in zero_columns:
        for i in range(m):
            l_2d[i][column] = 0

if __name__ == "__main__":
    field = [[1] * 10 for i in range(10)]
    field[1][1] = 0
    print(np.asarray(field))
    ans_func(field)
    print(np.asarray(field))



