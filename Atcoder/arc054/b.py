p = float(input())

low = 0
high = 100

def f(x):
    return x + p * 2 ** (-x/1.5)

while high - low > 0.000000001:
    mid_left = (low*2 + high) / 3
    mid_right = (low + high * 2) / 3

    if f(mid_left) >= f(mid_right):
        low = mid_left
    else:
        high = mid_right
print(f(high))

