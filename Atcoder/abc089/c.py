import itertools


n = int(input())
s = [input() for _ in range(n)]

m = 0
a = 0
r = 0
c = 0
h = 0

for i in range(len(s)):
    if s[i][0] == "M":
        m += 1
    if s[i][0] == "A":
        a += 1
    if s[i][0] == "R":
        r += 1
    if s[i][0] == "C":
        c += 1
    if s[i][0] == "H":
        h += 1

head_l = [m, a, r, c, h]
comb_l = list(itertools.combinations(head_l, 3))
ans = 0
for comb in comb_l:
    pat = comb[0]
    for i in range(1, len(comb)):
        pat *= comb[i]
    ans += pat
        
print(ans)
        





