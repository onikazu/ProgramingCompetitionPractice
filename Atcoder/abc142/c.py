n = int(input())
A = list(map(int, input().split()))

ans = [0] * n

for i in range(n):
    s = A[i]
    ans[s-1] = i+1
print(*ans)
