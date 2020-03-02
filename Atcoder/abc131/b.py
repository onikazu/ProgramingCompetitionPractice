n, l = list(map(int, input().split()))

apples = [l+i-1 for i in range(1, n+1)]
del apples[list(map(abs, apples)).index(min(list(map(abs, apples))))]
print(sum(apples))

