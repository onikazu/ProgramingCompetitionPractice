n = int(input())
h = list(map(int, input().split()))
prev = 10 ** 9 + 2
for i in reversed(range(len(h))):
    if h[i] < (prev + 1):
        prev = h[i]
        continue
    elif h[i] == (prev + 1):
        prev = h[i] - 1
    else:
        print("No")
        exit(1)
print("Yes")

