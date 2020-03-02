n = int(input())
h_l = []
s_l = []
hs_max_l = [] # to calculate max range of binary search
for _ in range(n):
    h, s = map(int, input().split())
    h_l.append(h)
    s_l.append(s)
    hs_max_l.append(h+(n-1) * s)

low = max(h_l)
high = max(hs_max_l)

def check(height):
    limit_times = []
    for i in range(n):
        limit_times.append((height-h_l[i]) // s_l[i])
    limit_times = sorted(limit_times)
    
    for i in range(n):
        if limit_times[i] < i:
            return False
    return True

if check(low):
    print(low)
    exit()

while high - low > 1:
    mid = (low + high) // 2

    # check 
    if check(mid):
        high = mid
    else:
        low = mid
print(high)
