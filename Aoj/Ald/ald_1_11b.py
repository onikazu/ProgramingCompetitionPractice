n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

for i in range(len(l)):
    if len(l[i]) == 2:
        l[i] = []
    else:
        l[i] = l[i][2:]

d = [0] * n
f = [0] * n

d[0] = 1

stack = [0]

while stack:
    check


