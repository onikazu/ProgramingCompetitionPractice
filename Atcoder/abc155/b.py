import sys

n = int(input())
a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] % 2 == 0:
        if a[i] % 3 == 0 or a[i] % 5 == 0:
            pass
        else:
            print("DENIED")
            sys.exit(0)
print("APPROVED")

