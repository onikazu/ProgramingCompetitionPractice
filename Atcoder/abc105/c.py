n = int(input())
ans = []

if n == 0:
    print(0)
    exit()

while n != 0:
    r = N % 2
    r = abs(r)
    n = (n - r) // -2
    ans.append(str(r))

ans.reverse()
print(''.join(ans))

