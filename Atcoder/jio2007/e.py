r, c = map(int, input().split())
senbei = [list(map(int, input().split())) for _ in range(r)]

def flip_row(row):
    res = []
    for v in row:
        if v == 0:
            res.append(1)
        else:
            res.append(0)
    return res

ans = 0
for i in range(1 << r):
    senbei_copy = senbei.copy()
    flip_idx = []
    # flipするindexをbit全探索
    for j in range(r):
        if (i >> j) & 1 == 1:
            flip_idx.append(j)

    for j in flip_idx:
        senbei_copy[j] = flip_row(senbei_copy[j])

    num_can_ship = 0
    for j in range(c):
        cnt_z = 0
        cnt_o = 0
        for k in range(r):
            if senbei_copy[k][j] == 0:
                cnt_z += 1
            else:
                cnt_o += 1
        num_can_ship += max(cnt_o, cnt_z)
    ans = max(ans, num_can_ship)
print(ans)
        

    
    

    



        

