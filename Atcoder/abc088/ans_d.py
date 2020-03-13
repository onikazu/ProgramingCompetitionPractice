# https://atcoder.jp/contests/abc088/submissions/10568858
from collections import deque
from sys import setrecursionlimit

setrecursionlimit(10 ** 9)

H, W = map(int, input().split())
field = [list(input()) for i in range(H)]

queue = deque([])
seen = [[0] * W for _ in range(H)]
prev_x = [[0] * W for _ in range(H)]
prev_y = [[0] * W for _ in range(H)]
direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]

def bfs(y, x):
    queue.append([y, x])
    seen[y][x] = 1
    prev_x[y][x] = -1
    prev_y[y][x] = -1

    while queue:
        y, x = queue.popleft()

        for dy, dx in direction:
            next_x = x + dx
            next_y = y + dy

            if 0 <= next_x < W and 0 <= next_y < H and field[next_y][next_x] == "." and seen[next_y][next_x] == 0:
                seen[next_y][next_x] = 1
                prev_x[next_y][next_x] = x
                prev_y[next_y][next_x] = y
                queue.append([next_y, next_x])

shortest_path = [[0] * W for i in range(H)]


