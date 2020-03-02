n = int(input())
s = input()

prev_s = ""
ans = 0

for i in range(n):
    if s[i] != prev_s:
        ans += 1
        prev_s = s[i]
print(ans)
