s = input()
t = input()

ans = False
for i in range(len(s)):
    rotated_s = ""
    if i == 0:
        rotated_s = s[i:-1] + s[-1]
    else:
        rotated_s = s[i:-1]+ s[-1] + s[0:i]
    
    if rotated_s == t:
        ans = True

if ans is True:
    print("Yes")
else:
    print("No")


