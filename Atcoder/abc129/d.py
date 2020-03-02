h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
cnt = [[0] * w for _ in range(h)]

def rotate(l_2d):
    l_2d = np.array(l_2d)
    return (l_2d.T).tolist()


# check horizontal direction(done)
done = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if done[i][j] == 1 or s[i][j] == "#":
            continue
        l = 0
        k = j
        while k < w:
            if s[i][k] == ".":
                l += 1
            else:
                break
            k += 1
        for o in range(l):
            cnt[i][j+o] += l
            done[i][j+o] = 1


# check vertical direction
done = [[0] * w for _ in range(h)]
for j in range(w):
    for i in range(h):
        if done[i][j] == 1 or s[i][j] == "#":
            continue
        l = 0
        k = i
        while k < h:
            if s[k][j] == ".":
                l += 1
            else:
                break
            k += 1
        for o in range(l):
            cnt[i+o][j] += l
            done[i+o][j] = 1

print(max(list(map(max, cnt))) - 1)

