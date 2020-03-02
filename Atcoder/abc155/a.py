a, b, c = list(map(int, input().split()))

if a == b and b == c:
    print("No")
elif a == b:
    print("Yes")
elif b == c:
    print("Yes")
elif a == c:
    print("Yes")
else:
    print("No")

    

