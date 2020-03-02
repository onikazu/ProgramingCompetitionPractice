class UnionFind:
    def __init__(self, n):
        # 最初はすべてが根。ノード番号は1からかいしするのでインデックスもそれに合わせる
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        # 入力の根を返す
        if self.par[x] == x:
            return x
        else:
            # 親の書き換えによる高速化
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_chack(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1






