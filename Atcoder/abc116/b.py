b = int(input())

a = [b]
prev = b
idx = 1
while True:
    fa = prev // 2 if prev % 2 == 0 else 3 * prev +1 
    if fa in a:
        print(len(a) + 1)
        break
    a.append(fa)
    prev = fa
