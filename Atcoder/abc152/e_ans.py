n = int(input())
a = list(map(int, input().split()))

# aの最小公倍数を求めればおｋ
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

a_factrized = list(map(factorization, a))

d = {}

for i in range(len(a_factrized)):
    for j in range(len(a_factrized[i])):
        num = a_factrized[i][j][0]
        num_cnt = a_factrized[i][j][1]
        tmp = d.get(num, 0)
        if tmp < num_cnt:
            d[num] = num_cnt

tmp = 1
for k in d.keys():
    tmp *= d[k] * k

ans = 0

for i in range(len(a)):
    ans += tmp // a[i]
print(ans % (10 ** 9 + 7))


