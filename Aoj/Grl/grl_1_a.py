from heapq import heappush, heappop

INF = float("inf")


v_num, e_num, r = list(map(int, input().split()))
edges_l = [[] for _ in range(v_num)]
dist_l = [INF for _ in range(v_num)]

for _ in range(e_num):
    s, t, dist = map(int, input().split())
    edges_l[s].append((t, dist))

que = []
heappush(que, (0, r))
dist_l[r] = 0

while que:
    dist, node = heappop(que)
    for to, cost in edges_l[node]:
        if dist_l[to] > cost + dist:
            dist_l[to] = cost + dist
            heappush(que, (cost + dist, to))

for dist in dist_l:
    if dist == INF:
        print("INF")
    else:
        print(dist)
