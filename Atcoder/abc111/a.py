s = input()
ans = ""

for i in range(len(s)):
    if s[i] == "1":
        ans += "9"
    else:
        ans += "1"
print(int(ans))
