from collections import deque


n, m, k = list(map(int, input().split()))
friends = [tuple(map(int, input().split())) for _ in range(m)]
block = [tuple(map(int, input().split())) for _ in range(k)]

relation_d = {}
for i in range(1, n+1):
    relation_d[str(i)] = set()
for a, b in friends:
    relation_d[str(a)].add(str(b))
    relation_d[str(b)].add(str(a))

block_d = {}
for i in range(1, n+1):
    block_d[str(i)] = set()
for a, b in block:
    block_d[str(a)].add(str(b))
    block_d[str(b)].add(str(a))


for i in range(1, n+1):
    visited = set()
    candidates = set()
    dq = deque(list(relation_d[str(i)]))
    while dq:
        for j in range(len(dq)):
            node = dq.popleft()
            if not node in relation_d[str(i)]:
                candidates.add(node)
            if not node in visited:
                dq.extend(relation_d[node])
            visited.add(node)
    candidates.discard(str(i))
    print(len(candidates-block_d[str(i)]-set(str(i))), end=" ")

    #print(relation_d[str(i)], block_d[str(i)], relation_d[str(i)]-block_d[str(i)])
    # print(len(candidates-block_d[str(i)]))
    # print(len(member-relation_d[str(i)]-block_d[str(i)])-1, end=" ")
    # print(n-1-len(relation_d[str(i)]-block_d[str(i)]), end=" ")

