n, m, x = list(map(int, input().split()))
A = list(map(int, input().split()))

zero_g = 0
n_g = 0

for i in range(len(A)):
    if A[i] < x:
        zero_g += 1
    else:
        n_g += 1
print(min(n_g, zero_g))
