def time_str2sec(time_str):
    h, m, s = time_str.split(":")
    res = time2int(h) * 3600 + time2int(m) * 60 + time2int(s)
    return res

def time2int(time):
    if time[0] == "0":
        return int(time[1])
    else:
        return int(time)

data_set = []
while True:
    n = int(input())
    if n == 0:
        break
    time_sch = [list(map(time_str2sec, input().split())) for _ in range(n)]
    data_set.append(time_sch)

for i in range(len(data_set)):
    cul_sum = [0] * (24 * 3600 + 1)
    for dep, arrival in data_set[i]:
        cul_sum[dep] += 1
        cul_sum[arrival] -= 1

    for j in range(len(cul_sum)-1):
        cul_sum[j+1] += cul_sum[j]

    print(max(cul_sum))

