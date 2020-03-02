import sys
from collections import defaultdict

S = input()
T = input()
L = len(S)

# 置換辞書
# 一対一対応になっているか走査する
dds = defaultdict(int)
ddt = defaultdict(int)
for i in range(L):
    # i文字目
    s = S[i]
    t = T[i]
    if dds[s] == 0:
        dds[s] = t
    else:
        if dds[s] != t:
            print("No")
            sys.exit()
    if ddt[t] == 0:
        ddt[t] = s
    else:
        if ddt[t] != s:
            print("No")
            sys.exit()
print("Yes")

