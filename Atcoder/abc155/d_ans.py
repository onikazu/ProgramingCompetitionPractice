n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)

nc = 0
zc = 0
pc = 0

# count negative value, zero and positive value
for i in range(n):
    if arr[i] < 0:
        nc += 1
    elif arr[i] == 0:
        zc += 1
    else:
        pc += 1

# count negative pair and so on 
ncc = nc * pc
zcc = zc * (nc + pc) + (zc * (zc - 1)) // 2
pcc = (nc * (nc - 1)) // 2 + (pc * (pc - 1)) // 2

# when k is less than ncc
if k <= ncc:
    # sort absolute value
    arr1 = [] # negative absolute
    arr2 = []
    for i in range(n):
        if arr[i] < 0:
            arr1.append(-arr[i])
        elif arr[i] > 0:
            arr2.append(arr[i])
    arr1 = arr1[::-1]
    c1 = len(arr1)
    c2 = len(arr2)
    l = 0
    r = 10 ** 18 + 1
    k = ncc - k

    # binary search
    while r - l != 1:
        mid = (l + r) // 2
        cnt = 0
        pos = c2 - 1
        # しゃくとり法
        for i in range(c1):
            while pos != -1:
                if arr2[pos] > mid // arr1[i]:
                    pos -= 1
                else:
                    break
            cnt += pos + 1
        if cnt > k:
            r = mid
        else:
            l = mid
    print(-r)
elif k <= (ncc + zcc):
    print(0)
else:
    arr1 = []
    arr2 = []
    for i in range(n):
        if arr[i] < 0:
            arr1.append(-arr[i])
        elif arr[i] > 0:
            arr2.append(arr[i])
    arr1 = arr1[::-1]
    c1 = len(arr1)
    c2 = len(arr2)
    l = 0
    r = 10 ** 18 + 1
    k -= (ncc + zcc)
    while r - l != 1:
        mid = (l + r) // 2
        cnt1 = 0
        pos1 = c1 - 1
        for i in range(c1):
            tmp = 0
            while pos1 != -1:
                if arr1[pos1] > mid // arr1[i]:
                    pos1 -= 1
                else:
                    break
            tmp += pos1 + 1
            if arr1[i] ** 2 < mid:
                tmp -= 1
            cnt1 += tmp
        cnt1 = cnt1 // 2
        cnt2 = 0
        pos2 = c2 - 1
        for i in range(c2):
            tmp = 0
            while pos2 != -1:
                if arr2[pos2] > mid // arr2[i]:
                    pos2 -= 1
                else:
                    break
            tmp += pos2 + 1
            if arr2[i] ** 2 < mid:
                tmp -= 1
            cnt2 += tmp
        cnt2 = cnt2 // 2
        cnt = cnt1 + cnt2
        if cnt >= k:
            r = mid
        else:
            l = mid
    print(r)


        



