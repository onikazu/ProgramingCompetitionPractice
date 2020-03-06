n = int(input())
graph = [[]]

for _ in range(n):
    info = map(int, input().split())
    if info[1] == 0:
        graph.append([])
    else:
        graph.append(info[2:])
        
d_l = [-1] * (n+1)
f_l = [-1] * (n+1)
time = 0

def dfs(v):
    if not v:
        return



