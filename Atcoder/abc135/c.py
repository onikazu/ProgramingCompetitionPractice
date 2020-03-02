n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

amari = 0
cnt = 0
for i in range(n):
    if a[i] >= b[i] + amari:
        cnt += b[i] + amari
    else:
        cnt += a[i]
        
    if amari > a[i]:
        amari = b[i]
    elif amari + b[i] > a[i]:
        amari = amari+b[i] - a[i]
    else:
        amari = 0

cnt += a[n] if amari >= a[n] else amari

print(cnt)

