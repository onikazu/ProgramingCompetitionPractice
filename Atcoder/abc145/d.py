x, y = list(map(int, input().split()))

def dfs(i, j):
    if i > x or j > y:
        return 0

    if i == x and j == y:
        return 1
    
    return dfs(i + 1, j + 2) + dfs(i + 2, j + 1)

print(dfs(0, 0))
