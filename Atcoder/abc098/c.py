n = int(input())
s = input()

e_l = [0]
w_l = [0]

for i in range(len(s)):
    if s[i] == "E":
        e_l.append(e_l[i]+1)
    else:
        e_l.append(e_l[i])

for i in range(len(s)):
    if s[i] == "W":
        w_l.append(w_l[i]+1)
    else:
        w_l.append(w_l[i])

ans = float("inf")
for i in range(len(s)):
    if i == 0:
        tmp = 0 + (e_l[-1] - e_l[i+1])
    elif i == len(s) - 1:
        tmp = w_l[i-1] 
    else:
        tmp = w_l[i -1] + (e_l[-1] - e_l[i+1])
    ans = min(ans, tmp)
print(ans)


