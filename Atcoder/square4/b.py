n, k = map(int, input().split())
a = list(map(int, input().split()))

# prob1
"""
ans = 0
for i in range(1, len(a)):
    ans += max(a[i-1]-a[i]+1, 0)
    a[i] += max(a[i-1]-a[i]+1, 0)
print(ans)
"""

ans = float("inf")
for i in range(1 << (n - 1)):
    a_copied = a.copy()
    comb = [0]
    cost = 0
    for j in range(n-1):
        if (i >> j) & 1 == 1:
            comb.append(1)
        else:
            comb.append(0)
    if sum(comb) < k - 1:
        continue
    
    for j in range(1, len(comb)):
        if comb[j] == 0:
            continue
        else:
            height = max(0, max(a_copied[:j])-a_copied[j]+1)   
            cost += height
            a_copied[j] += height 
    ans = min(cost, ans)
print(ans)

            



    



