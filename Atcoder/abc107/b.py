h, w = list(map(int, input().split()))

a = [input() for _ in range(h)]

flag = True
while True:
    for i in range(len(a)):
        if a[i] == w * '.':
            del a[i]
            h -= 1
            flag = False

    for i in range()

    if flag:
        break
        

