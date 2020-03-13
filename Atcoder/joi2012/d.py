import sys
from pprint import pprint
from collections import deque


W, H = map(int, sys.stdin.readline().split(" "))

grid = [[0 for _ in range(W+4)] for _ in range(H+4)]
for i in range(H):
    tmp = list(map(int, sys.stdin.readline().strip().split(" ")))
    grid[i+2][2:-2] = tmp

import numpy as np
print(np.asarray(grid))
q = deque()
q.append((0, 0))
visited = set()
ans = 0
delta = [((-1, 0), (0, -1), (1, -1), (1, 0), (0, 1), (1, 1)),
    ((-1, 0), (-1, -1), (0, -1), (1, 0), (-1, 1), (0, 1))]

while q:
    x, y = q.popleft()
    for dx, dy in delta[y % 2]:
        if 0 <= x+dx <= W+3 and 0 <= y+dy <= H+3:
            if grid[y+dy][x+dx] == 1:
                ans += 1
            else:
                if (x+dx, y+dy) in visited:
                    continue
                visited.add((x+dx, y+dy))
                q.append((x+dx, y+dy))
print(ans)

