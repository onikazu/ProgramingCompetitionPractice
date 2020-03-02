s = input()

len_l = []
ind_l = []
prev = "R"
cnt = 0
for i in range(len(s)):
    if prev == s[i]:
        cnt += 1
    else:
        ind_l.append(i - 1)
        prev = s[i]
        len_l.append(cnt)
        cnt = 1
len_l.append(cnt)
ind_l.append(len(s)-1)


ans = [0] * len(s)

tmp = 0
for i in range(0, len(ind_l), 2):
    rl_len = len_l[tmp] + len_l[tmp + 1]
    if rl_len % 2 == 0:
        ans[ind_l[i]] += rl_len // 2
        ans[ind_l[i+1]] += rl_len // 2
    else:
        if len_l[tmp] < len_l[tmp + 1]:
            ans[ind_l[i]] += rl_len // 2 + 1
            ans[ind_l[i+1]] += rl_len // 2
        elif len_l[tmp] > len_l[tmp + 1]:
            ans[ind_l[i]] += rl_len // 2
            ans[ind_l[i+1]] += rl_len // 2 + 1
    tmp += 2

for i in range(len(ans)):
    print(ans[i], end=" ")

