n = int(input())

ans = float('inf')
for a in range(1, int(n**(1/2)) + 1):
    if n % a != 0:
        continue
    b = n // a
    ans = min(ans, a+b-2)
print(ans)


