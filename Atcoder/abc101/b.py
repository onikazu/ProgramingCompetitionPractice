n = input()
n_i = int(n)

sn = 0
for i in range(len(n)):
    keta = int(n[i])
    sn += keta

if n_i % sn == 0:
    print("Yes")
else:
    print("No")
