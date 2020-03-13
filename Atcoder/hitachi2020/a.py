s = input()

if len(s) % 2 == 1:
    print('No')
    exit()

i = 0
while True:
    if i > len(s) - 2:
        break
    target = s[i:i+2]
    if target != "hi":
        print("No")
        exit()
    i += 2
print("Yes")




