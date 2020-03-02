import collections


n = int(input())
w_l = [input() for _ in range(n)]

counter = collections.Counter(w_l)

c_l = counter.most_common()
max_v = c_l[0][1]
ans_l = []
for i in range(len(c_l)):
    word, num = c_l[i]
    if max_v != num:
        break
    ans_l.append(word)

ans_l.sort()
for ans in ans_l:
    print(ans)





