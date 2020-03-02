n, m = list(map(int, input().split()))
q = []
r = []
for _ in range(m):
    sub = input().split()
    q.append(int(sub[0]))
    r.append(sub[1])

subs = {"q": q, "r": r}
ac = {}
num_ac = 0
num_penalty = 0

for i in range(m):
    if subs["r"][i] == "AC":
        if not subs["q"][i] in ac:
            num_ac += 1
            num_penalty += ac[subs["q"][i]]
    else:
        if not subs["q"][i] in ac:
            if ac.get(subs["q"][i], 0) == 0:
                ac[subs["q"][i]] = 1
            else:
                ac[subs["q"][i]] += 1
print(num_ac, num_penalty)




