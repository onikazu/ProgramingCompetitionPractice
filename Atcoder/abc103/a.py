A = list(map(int, input().split()))

ans = float("inf")
for i in range(len(A)):
    for j in range(len(A)):
        for k in range(len(A)):
            if i == j or j == k or k == i:
                continue
            tmp = abs(A[j] - A[i]) + abs(A[k] - A[j])
            ans = min(ans, tmp)
print(ans)


