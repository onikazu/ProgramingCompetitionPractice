a, b = list(map(int, input().split()))

a_height = 0
ab_gap = b - a
for i in range(ab_gap):
    a_height += i

print(a_height - a)
