a, b, k = list(map(int, input().split()))

ans_l = []
for i in range(k):
    if b >= a+i:
        ans_l.append(a+i)

for i in reversed(range(k)):
    if a <= b-i:
        ans_l.append(b-i)
    
ans_l = sorted(list(set(ans_l)))
for i in range(len(ans_l)):
    print(ans_l[i])

