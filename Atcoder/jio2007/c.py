points = []

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

points_set = set(points)
ans = 0

for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        p1_x, p1_y = points[i]
        p2_x, p2_y = points[j]
        p3_x, p3_y = p2_x-p2_y+p1_y, p2_y+p2_x-p1_x
        p4_x, p4_y = p1_x-p2_y+p1_y, p1_y+p2_x-p1_x
        if (p3_x, p3_y) in points_set and (p4_x, p4_y) in points_set:
            s = (p1_x-p2_x) ** 2 + (p1_y-p2_y) ** 2
            ans = max(s, ans)
print(ans)
