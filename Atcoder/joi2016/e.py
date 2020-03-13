from heapq import heappush, heappop


INF = float("inf")
n, m, k, s = map(int, input().split())
p, q = map(int, input().split())
c = set([int(input()) for _ in range(k)])
fros, tos = [], []

graph_alt = [[] for _ in range(n)]

graph = [[] for _ in range(n)]
for _ in range(m):
    fro, to = map(int, input().split())
    fros.append(fro)
    tos.append(to)
    graph_alt[fro-1].append(to-1)
    graph_alt[to-1].append(fro-1)

danger_towns = set()
for t in c:
    danger_towns = danger_towns | set(graph_alt[t-1])

for i in range(m):
    fro = fros[i]
    to = tos[i]
    if to in c: 
        graph[fro-1].append((to-1, INF))
    elif to in danger_towns:
        graph[fro-1].append((to-1, q))
    else:
        graph[fro-1].append((to-1, p))

    if fro in c:
        graph[to-1].append((fro-1, INF))
    elif to in danger_towns:
        graph[to-1].append((fro-1, q))
    else:
        graph[to-1].append((fro-1, p))

import numpy as np
print(np.asarray(graph))

INF = float("inf")
dist_l = [INF for _ in range(n)]
que = []
heappush(que, (0, 0))
dist_l[0] = 0

while que:
    dist, node = heappop(que)
    for to, cost in graph[node]:
        if dist_l[to] > cost + dist:
            dist_l[to] = cost + dist
            heappush(que, (cost+dist, to))

print(dist_l)
print(dist_l[-1])


