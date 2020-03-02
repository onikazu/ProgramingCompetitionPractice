n, m = list(map(int, input().split()))
# [[preficture, year, num]...]
towns = [list(map(int, input().split())) + [i] for i in range(m)]
sort_towns = sorted(towns, key = lambda x : (x[0], x[1]))

prev_pref = 1
town_no = 1
for i in range(len(sort_towns)):
    pref = sort_towns[i][0]
    town = sort_towns[i][1]
    if not prev_pref == pref:
        town_no = 1
        prev_pref = pref
        sort_towns[i].append(town_no)
    sort_towns[i].append(town_no)
    town_no += 1
sort_towns = sorted(sort_towns, key=lambda x : x[2])
for i in range(len(sort_towns)):
    print(str(sort_towns[i][0]).zfill(6) + str(sort_towns[i][3]).zfill(6))



