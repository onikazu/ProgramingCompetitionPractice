s = input()

s = s.split("/")
temp = ["01", "02", "03", "04"]

if int(s[0]) < 2019:
    print("Heisei")
elif int(s[0]) == 2019 and s[1] in temp:
    print("Heisei")
else:
    print("TBD")

