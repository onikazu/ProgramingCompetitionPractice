n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
prev_a = -1
for a in A:
    ans += B[a - 1] 
    if a - prev_a == 1:
        ans += C[prev_a - 1]
    prev_a = a
print(ans)
