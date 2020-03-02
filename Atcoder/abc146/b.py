n= int(input())
s = input()

# ord(A) -> 65, ord(Z) -> 90

ans = ""
for i in range(len(s)):
    chr_num = ord(s[i]) + n
    if chr_num > 90:
        chr_num = (chr_num % 90) + 64
    ans += chr(chr_num)
print(ans)

