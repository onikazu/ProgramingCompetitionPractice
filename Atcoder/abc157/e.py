n = int(input())
s = list(input())
q_num = int(input())
query = []
for _ in range(q_num):
    query.append(input().split())


for q, i, j in query: 
    if q == "1":
        i = int(i)
        s[i-1] = j
    else:
        i = int(i)
        j = int(j)
        print(len(set(s[i-1:j])))



