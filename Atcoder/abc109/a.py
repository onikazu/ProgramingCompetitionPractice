a, b = list(map(int, input().split()))

ans = "No"
for c in range(1, 4):
    if a * b * c % 2 == 1:
        ans = "Yes"
        break
print(ans)

