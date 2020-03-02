n, x = list(map(int, input().split()))
l_l = list(map(int, input().split()))

count = 1
dist = 0
for l in l_l:
    dist += l
    if dist > x:
        break
    else:
        count += 1

print(count)

