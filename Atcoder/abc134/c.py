n = int(input())
a = [int(input()) for _ in range(n)]

sorted_a = sorted(a)
first_a = sorted_a[-1]
second_a = sorted_a[-2]

for i in range(len(a)):
    if a[i] == first_a:
        print(second_a)
    else:
        print(first_a)

