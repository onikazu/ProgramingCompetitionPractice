s = input()
ans = 0

def check(sub):
    check_s = set(list("ACGT"))
    for c in sub:
        if not c in check_s:
            return 0
    return len(sub)    
    
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        ans = max(ans, check(s[i:j]))

print(ans)
