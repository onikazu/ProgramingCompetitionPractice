import numpy as np


def brute_force(l_2d):
    for i in range(len(l_2d)-1):
        for j in range(i+1, len(l_2d[0])):
            l_2d[i][j], l_2d[j][i] = l_2d[j][i], l_2d[i][j]


if __name__ == "__main__":
    l_2d = [[i for i in range(32)] for _ in range(32)]
    print(np.asarray(l_2d))
    brute_force(l_2d)
    print(np.asarray(l_2d))

