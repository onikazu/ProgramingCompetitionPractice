s = int(input())

def check_target(s):
    s = str(s)
    prev = s[0]
    for i in range(len(s)):
        if s[0] != s[i]:
            return False
    return True

ans = 0
for i in range(s, 1000):
    if check_target(i):
        ans = i
        break

print(ans)
