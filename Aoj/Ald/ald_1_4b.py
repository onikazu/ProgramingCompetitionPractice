n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

"""use set 
ans = 0
s = set(s)
for i in range(len(t)):
    if t[i] in s:
        ans += 1
print(ans)

"""

def find_num(num):
    l = 0
    r = len(s) - 1
    while l <= r:
        mid = (l+r) // 2
        if s[mid] == num:
            return True
        elif s[mid] < num:
            l = mid+1
        else:
            r = mid-1
    return False

ans = 0
for num in t:
    ans += 1 if find_num(num) is True else 0
print(ans)



