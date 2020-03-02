n, m, k = list(map(int, input().split()))
friends = [tuple(map(int, input().split())) for _ in range(m)]
block = [tuple(map(int, input().split())) for _ in range(k)]

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same(self, x, y):
        x = self.find(x)
        y = self.find(y)
        return x == y

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    
    def get_group(self, x):
        x = self.find(x)
        return set([node+1 for node in range(n) if x == self.find(node+1)])

union_find = UnionFind(n)

for f1, f2 in friends:
    union_find.union(f1, f2)

block_d = {}
for i in range(1, n+1):
    block_d[str(i)] = set()
for b1, b2 in block:
    block_d[str(b1)].add(b2)
    block_d[str(b2)].add(b1)

friends_d = {}
for i in range(1, n+1):
    friends_d[str(i)] = set()
for f1, f2 in friends:
    friends_d[str(f1)].add(f2)
    friends_d[str(f2)].add(f1)

groups = []
for i in range(1, n+1):
    target_group = None
    for group in groups:
        if i in group:
            target_group = group
            break
    if target_group is None:
        target_group = union_find.get_group(i)
    print(len(target_group-block_d[str(i)]-friends_d[str(i)])-1, end=" ")






