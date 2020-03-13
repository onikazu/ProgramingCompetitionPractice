from collections import deque


n = int(input())
graph = [[] for _ in range(n)]
INF = float("inf")

for _ in range(n):
    info = list(map(int, input().split()))
    node_id = info[0]
    k = info[1]
    if k == 0:
        continue
    for node in info[2:]:
        graph[node_id-1].append(node-1)

dist_l = [INF for _ in range(n)]
done_l = [0 for _ in range(n)]
dist_l[0] = 0
done_l[0] = 1
que = deque([0])

dist = 1
while que:
    for i in range(len(que)):
        target = que.popleft()
        nodes = graph[target]
        for node in nodes:
            if dist_l[node] > dist:
                dist_l[node] = dist
            if done_l[node] == 0:
                que.append(node)
                done_l[node] = 1
    dist += 1

for i, d in enumerate(dist_l):
    d = -1 if d == INF else d
    print(i+1, d)

    






