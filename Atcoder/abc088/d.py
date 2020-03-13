from collections import deque


h, w = map(int, input().split())
field = [list(input()) for _ in range(h)]
INF = float("inf")
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

done = [[0] * w for _ in range(h)]
done[0][0] = 1

que = deque([(0, 0)])

dist = 0 
flag = False
while que:
    dist += 1

    for i in range(len(que)):
        x, y = que.popleft()
        if x == w-1 and y == h-1:
            flag = True
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < w and 0 <= ny < h and done[ny][nx] == 0 and field[ny][nx] == ".":
                que.append((nx, ny))
                done[ny][nx] == 1
    if flag:
        break

if not flag:
    print(-1)
    exit()

white_num = 0
for i in range(h):
    for j in range(w):
        if field[i][j] == ".":
            white_num += 1
print(white_num-dist)



