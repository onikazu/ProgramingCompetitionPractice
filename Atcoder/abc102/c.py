n = int(input())
A = list(map(int, input().split()))

B = [A[i] - (i + 1) for i in range(len(A))]
B = sorted(B)
if len(B) % 2 == 1:
    print(B[len(B) // 2])
else:
    print(B[len(B) // 2] + B)
