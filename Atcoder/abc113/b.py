n = int(input())
t, a = list(map(int, input().split()))
h = list(map(int, input().split()))

gap = [abs(a - (t - h[i] * 0.006)) for i in range(n)]
print(gap.index(min(gap)) + 1)


