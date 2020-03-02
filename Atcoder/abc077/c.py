n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))

def check_a(a_num, b_num):
    res = False
    if a_num < b_num:
        res = True
    return res

def check_c(c_num, b_num):
    res = False
    if b_num < c_num:
        res = True
    return res

ans = 0
cnt_a = 0
cnt_c = 0
for bi in range(len(b)):
    left = 0
    right = len(a)-1
    if check_a(a[0], b[bi]) is False:
        cnt_a = 0
    elif check_a(a[-1], b[bi]) is True:
        cnt_a = len(a)
    else:
        while right-left > 1:
            mid = (left + right) // 2
            if check_a(a[mid], b[bi]):
                left = mid
            else:
                right = mid
        cnt_a = left + 1

    left = 0
    right = len(c) - 1
    if check_c(c[0], b[bi]) is True:
        cnt_c = len(c)
    elif check_c(c[-1], b[bi]) is False:
        cnt_c = 0
    else:
        while right - left > 1:
            mid = (left + right) // 2
            if check_c(c[mid], b[bi]):
                right = mid
            else:
                left = mid
        cnt_c = len(c) - right
    ans += cnt_a * cnt_c
print(ans)

