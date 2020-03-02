h, w = list(map(int, input().split()))
s = [list(input()) for _ in range(h)]

def dfs(i, j, maze, ans):
    if i < 0 or j < 0 or i >= len(maze) or j >= len(maze[0]):
        return ans
    elif maze[i][j] == "#": 
        return ans
    else:
        maze[i][j] = "#"
        directions  = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
        ret = 0
        for direction in directions:
            ret = max(ret, dfs(direction[0], direction[1], maze, ans+1))
        return ret

ret = 0
for i in range(len(s)):
    for j in range(len(s[0])):
        maze = s.copy()
        print(dfs(i, j, maze, 0))
        ret = max(ret, dfs(i, j, maze, 0))
print(ret)






