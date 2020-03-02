antenas = [int(input()) for _ in range(5)]
k = int(input())
if antenas[-1] - antenas[0] <= k:
    print("Yay!")
else:
    print(":(")



