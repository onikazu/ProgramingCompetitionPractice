# グラフ木累積和
n, q = map(int, input().split())
tree = [[] for _ in range(n)]
ans = [0] * n

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

for _ in range(q):
    p, x = map(int, input().split())
    p -= 1
    ans[p] += x

def dfs(v, p=-1):
    for u in tree[v]:
        # 親には戻らないようにする
        if u == p:
            continue
        ans[u] += ans[v]
        dfs(u, v)

dfs(0)
print(*ans)

