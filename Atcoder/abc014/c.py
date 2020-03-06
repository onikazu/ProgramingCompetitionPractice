n = int(input())
users = [tuple(map(int, input().split())) for _ in range(n)]

colors = [0] * (1000001 + 1)

for a, b in users:
    colors[a] += 1
    colors[b+1] -= 1

for i in range(0, len(colors)-1):
    colors[i+1] += colors[i]

print(max(colors))
