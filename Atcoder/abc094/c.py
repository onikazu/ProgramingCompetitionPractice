n = int(input())
x = list(map(int, input().split()))

x_sorted = sorted(x)
larger_candidate = x_sorted[n//2]
smaller_candidate = x_sorted[n//2-1]

for i in range(len(x)):
    if x[i] <= smaller_candidate:
        print(larger_candidate)
    else:
        print(smaller_candidate)



