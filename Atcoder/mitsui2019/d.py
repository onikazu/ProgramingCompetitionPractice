n = int(input())
s = input()

ans = 0

for i in range(0, 1000):
    target = str(i).zfill(3)
    target_idx = 0
    for c in s:
        if c == target[target_idx]:
            target_idx += 1
        if target_idx == 3:
            ans += 1
            break
print(ans)



