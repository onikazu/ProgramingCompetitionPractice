import sys
sys.setrecursionlimit(100000)
w_l = []
h_l = []
m_l = []


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    w_l.append(w)
    h_l.append(h)
    m_l.append([list(map(int, input().split())) for _ in range(h)])

for i in range(len(w_l)):
    w = w_l[i]
    h = h_l[i]
    m = m_l[i]
    def dfs(i, j):
        if i < 0 or i >= h or j < 0 or j >= w:
            return
        if m[i][j] == 0:
            return 
        else:
            m[i][j] = 0
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j+1)
            dfs(i-1, j-1)
            dfs(i-1, j+1)
            dfs(i+1, j-1)

    ans = 0
    for i in range(h):
        for j in range(w):
            if m[i][j] == 1:
                ans += 1
                dfs(i, j)
    print(ans)







