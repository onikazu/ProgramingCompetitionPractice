A = list(map(int, input().split()))
k = int(input())
A[A.index(max(A))] *= 2 ** k

print(sum(A))
