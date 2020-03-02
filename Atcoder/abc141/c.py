n, k, q = list(map(int, input().split()))
A = [int(input()) for _ in range(q)]

P = [0] * n 
for a in A:
    P[a-1] += 1

for p in P:
    if p > len(A) - k:
        print("Yes")
    else:
        print("No")
        
