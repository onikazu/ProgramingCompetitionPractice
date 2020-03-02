k = int(input())

ans = 0
for i in range(1, k):
    for j in range(i+1, k+1):
        if (i + j) % 2 == 1:
            ans += 1

print(ans)

