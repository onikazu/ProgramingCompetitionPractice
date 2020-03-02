n = int(input())
s = input().split()

ans = "Three"
for i in range(len(s)):
    if s[i] == "Y":
        ans = "Four"
        break
        
print(ans)

