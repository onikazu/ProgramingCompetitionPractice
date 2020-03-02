s = input()

ans = 10000
for i in range(len(s)-2):
    retreive = int(s[i:i+3])
    gap = abs(retreive - 753)
    ans = min(gap, ans)
print(ans)

