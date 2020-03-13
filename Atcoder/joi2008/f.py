from heapq import heappop, heappush


INF = float("inf")
n, k = map(int, input().split())
graph = [[] for _ in range(n)]

def add_edge(fro, to, weight):
    # TODO: use hash table?
    graph[fro-1].append((to-1, weight))
    graph[to-1].append((fro-1, weight))


def calc_dist(start, goal):
    dist_l = [INF for _ in range(n)]
    que = []
    heappush(que, (0, start-1))
    while que:
        dist, node = heappop(que)
        for to, cost in graph[node]:
            if dist_l[to] > cost + dist:
                dist_l[to] = cost + dist
                heappush(que, (cost + dist, to))
    return -1 if dist_l[goal-1] == INF else dist_l[goal-1]


orders = [list(map(int, input().split())) for _ in range(k)]


for order in orders:
    if order[0] == 1:
        fro, to, weight = order[1:]
        add_edge(fro, to, weight)
    else:
        start, goal = order[1:]
        print(calc_dist(start, goal))


