h = int(input())

def calc(h):
    if h == 1:
        return 1
    else:
        return 2 * calc(h // 2) + 1
print(calc(h))
