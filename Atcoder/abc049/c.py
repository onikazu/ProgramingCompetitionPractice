s = list(input())
words = ["dream", "dreamer", "erase", "eraser"]
ans = True
while True:
    if s == []:
        print("YES")
        break
    if "".join(s[-5:]) == "dream":
        del s[-5:]
    elif "".join(s[-7:]) == "dreamer":
        del s[-7:]
    elif "".join(s[-5:]) == "erase":
        del s[-5:]
    elif "".join(s[-6:]) == "eraser":
        del s[-6:]
    else:
        print("NO")
        break


