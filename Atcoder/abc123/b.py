items = [int(input()) for _ in range(5)]
items = sorted(items, key=lambda x:x%10)
flag = False
for i in range(len(items)):
    if items[i] % 10 == 0:
        continue
    elif flag is False:
        flag = True
        continue
    tmp = items[i] // 10
    items[i] = tmp * 10 + 10


print(sum(items))
