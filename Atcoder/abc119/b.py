n = int(input())

otoshi = [list(input().split()) for _ in range(n)]

money = 0
for i in range(n):
    if otoshi[i][1] == "JPY":
        money += float(otoshi[i][0])
    else:
        money += float(otoshi[i][0]) * 380000.0

print(money)
