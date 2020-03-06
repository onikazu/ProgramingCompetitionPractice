from collections import deque


r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
m = [list(input()) for _ in range(r)]
count = [[-1] * c for _ in range(r)]


queue = deque([(sx-1, sy-1)])
time = 0

while queue:
    for i in range(len(queue)):
        x, y = queue.popleft()
        if x < 0 or x >= c or y < 0 or y >= r:
            continue
        if m[y][x] == "#":
            continue
        if count[y][x] != -1:
            continue
        else:
            count[y][x] = time
            queue.append((x+1, y))
            queue.append((x-1, y))
            queue.append((x, y+1))
            queue.append((x, y-1))
    time += 1

print(count[gy-1][gx-1])
