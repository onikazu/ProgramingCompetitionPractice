import sys


s = input()
k = int(input())

if s == "1" * len(s):
    print(1)

for i in range(len(s)):
    if s[i] != "1":
        print(s[i])
        sys.exit()
