n, m, x, y = list(map(int, input().split()))
x_l = list(map(int, input().split()))
y_l = list(map(int, input().split()))
x_l.append(x)
y_l.append(y)

x_max = max(x_l)
y_min = min(y_l)
print(x_max, y_min)
if y_min - x_max > 1:
    print("No War")
else:
    print("War")


