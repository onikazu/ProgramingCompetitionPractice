a, b = list(map(int, input().split()))

if (a - b) % 2 != 0:
    print("IMPOSSIBLE")
elif a >= b:
    print(int(a-((a-b)/2)))
else:
    print(int(b-((b-a)/2)))

