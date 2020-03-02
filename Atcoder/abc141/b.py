s = input()

is_yes = True
for i in range(len(s)):
    if (i+1)%2 == 0 and s[i] == "R":
        is_yes = False
        break

    if (i+1)%2 == 1 and s[i] == "L":
        is_yes = False
        break

if is_yes is True:
    print("Yes")
else:
    print("No")

