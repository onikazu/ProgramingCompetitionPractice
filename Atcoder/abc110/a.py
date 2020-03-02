given_list = list(map(int, input().split()))

given_list.sort()
given_list[-1] = given_list[-1] * 10
print(sum(given_list))

