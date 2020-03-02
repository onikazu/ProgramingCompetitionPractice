n = int(input())
p = [int(input()) for _ in range(n)]

p = sorted(p)
p[-1] = p[-1] // 2
print(sum(p))
