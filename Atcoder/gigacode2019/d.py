h, w, k, v = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(h)]

cul_sum = [[0] * (w + 1) for _ in range(h + 1)]

cul_sum[1][1] = A[0][0]

# generate culative sum 2d array
for i in range(2, len(cul_sum[0])):
    cul_sum[1][i] = cul_sum[1][i-1] + A[0][i-1]

for i in range(2, len(cul_sum)):
    cul_sum[i][1] = cul_sum[i-1][1] + A[i-1][0]

for i in range(2, len(cul_sum)):
    for j in range(2, len(cul_sum[0])):
        cul_sum[i][j] = cul_sum[i-1][j] + cul_sum[i][j-1] - cul_sum[i-1][j-1] + A[i-1][j-1]

max_s = 0
for i in range(1, h+1):
    for j in range(1, w+1):
        for ki in range(h-i+1):
            for l in range(w-j+1):
                price = cul_sum[ki+i][l+j] + cul_sum[ki][l] - cul_sum[ki][l+j] - cul_sum[ki+i][l]
                price += k * i * j
                if price <= v:
                    # print(f"price: {price}, (h, w): ({i}, {j}), (x, y): ({l}, {ki})")
                    max_s = max(max_s, i * j)
print(max_s)
