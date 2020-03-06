# おそらくpython だとnumpy 使わないとtle
r, c = map(int, input().split())
k = int(input())

import sys
input = sys.stdin.readline

m = [list(input())[:-1] for _ in range(r)]
q = [tuple(map(int, input().split())) for _ in range(k)]

j_m = [[0] * c for _ in range(r)]
o_m = [[0] * c for _ in range(r)]
i_m = [[0] * c for _ in range(r)]
maps = [j_m, o_m, i_m]

for i, target_c in enumerate(["J", "O", "I"]):
    for j in range(r):
        for l in range(c):
            if m[j][l] == target_c:
                maps[i][j][l] += 1

j_cum = [[0] * (c+1) for _ in range(r+1)]
o_cum = [[0] * (c+1) for _ in range(r+1)]
i_cum = [[0] * (c+1) for _ in range(r+1)]
cums = [j_cum, o_cum, i_cum]

# generate table
for i in range(3):
    for j in range(1, r+1):
        for l in range(1, c+1):
            if j == 1 and l == 1:
                cums[i][j][l] = maps[i][j-1][l-1]
            elif j == 1:
                cums[i][j][l] = maps[i][j-1][l-1] + cums[i][j][l-1]
            elif l == 1:
                cums[i][j][l] = maps[i][j-1][l-1] + cums[i][j-1][l]
            else:
                cums[i][j][l] = maps[i][j-1][l-1] + cums[i][j-1][l] + cums[i][j][l-1] - cums[i][j-1][l-1]

for y1, x1, y2, x2 in q:
    for i in range(3):
        cul_sum_map = cums[i]
        if i == 2:
            print(cul_sum_map[y2][x2]-cul_sum_map[y2][x1-1]-cul_sum_map[y1-1][x2]+cul_sum_map[y1-1][x1-1])
        else:
            print(cul_sum_map[y2][x2]-cul_sum_map[y2][x1-1]-cul_sum_map[y1-1][x2]+cul_sum_map[y1-1][x1-1], end=" ")



