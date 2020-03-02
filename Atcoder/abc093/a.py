s = input()
l = []
for i in range(len(s)):
    l.append(s[i])
l_s = set(l)

if len(l_s) == 3:
    print("Yes")
else:
    print("No")
