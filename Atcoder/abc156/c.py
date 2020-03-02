n = int(input())
x = list(map(int, input().split()))

ans = float("inf")

for i in range(min(x), max(x)+1):
    power = 0
    for j in range(len(x)):
        power += (x[j] - i) ** 2
    ans = min(ans, power)
print(ans)
        

