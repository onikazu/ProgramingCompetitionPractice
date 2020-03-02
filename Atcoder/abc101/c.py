n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

A_min_idx = A.index(min(A))

print(-(-(len(A)-1) // (k-1)) )

