import sys


n = int(input())
W = [input() for _ in range(n)]

w_set = set(W)
if len(w_set) != len(W):
    print("No")
    sys.exit()

prev = W[0]
for i in range(1, n):
    if W[i-1][-1] != W[i][0]:
        print("No")
        sys.exit()
print("Yes")


    


