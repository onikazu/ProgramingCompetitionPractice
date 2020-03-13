a, b = map(int, input().split())

for i in range(1, 2000):
    if int(i * 0.08) == a and int(i * 0.1) == b:
        print(i)
        exit()

print(-1)







"""
a_min = -(-a // 0.08)
a_max = -(-(a+1) // 0.08)
b_min = -(-b // 0.1)
b_max = -(-(b+1) // 0.1)

if a_max < b_min:
    print(-1)
elif a_min > b_min:
    print(int(a_min))
else:
    print(int(b_min))
"""



