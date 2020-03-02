import sys


n = int(input())

for i in range(100):
    for j in range(100):
        if i * 4 + j * 7 == n:
            print("Yes")
            sys.exit()
print("No")


