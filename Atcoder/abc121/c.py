n, m = list(map(int, input().split()))
store = [list(map(int, input().split())) for _ in range(n)]

store = sorted(store)

money = 0
items = 0

for i in range(len(store)):
    if items + store[i][1] >= m:
        money += store[i][0] * (m - items)
        break
    money += store[i][0] * store[i][1]
    items += store[i][1]

print(money)
