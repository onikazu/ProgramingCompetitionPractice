n = int(input())
a = [int(input()) for _ in range(n)]

max_i = 0
max_v = a[0]
for i in range(len(a)):
    if a[i] > max_v:
        max_v = a[i]
        max_i = i

a = a[max_i+1:] + a[:max_]

