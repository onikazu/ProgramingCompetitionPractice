n = input()

k = 0
if int(n[0]) < 3:
    k = 0
elif int(n[0]) < 5:
    k = 1
elif int(n[0]) < 7:
    k = 2
else:
    k = 3

ans = k * 3 ** (len(n)-1)
for keta in range(1, len(n)):
    ans += 3 ** keta
print(ans)
