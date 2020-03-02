n = int(input())
s = input()

ans = 0
for cut_point in range(1, n):
    first_half = s[:cut_point]
    second_half = s[cut_point:]
    ans = max(ans, len(set(first_half) & set(second_half)))
print(ans)
