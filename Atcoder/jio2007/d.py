m = int(input())
m_star = [tuple(map(int, input().split())) for _ in range(m)]
n = int(input())
n_star = [tuple(map(int, input().split())) for _ in range(n)]
n_star_set = set(n_star)

for i in range(len(n_star)):
    x_gap = n_star[i][0] - m_star[0][0]
    y_gap = n_star[i][1] - m_star[0][1]

    found = True
    for j in range(1, len(m_star)):
        if not (m_star[j][0]+x_gap, m_star[j][1]+y_gap) in n_star_set:
            found = False
            break
    if found:
        print(x_gap, y_gap)
        exit()
