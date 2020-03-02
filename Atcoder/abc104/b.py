S = input()

ans = True

tmp_S1 = ""
tmp_S2 = ""
for i in range(len(S)):
    if S[i] == "A" or S[i] == "C":
        continue
    tmp_S1 += S[i]
    tmp_S2 += S[i]

if tmp_S1.lower() != tmp_S2:
    ans = False

if S[0] != "A":
    ans = False

cnt = 0
for i in range(2, len(S)-1):
    if S[i] == "C":
        cnt += 1
if cnt != 1:
    ans = False

if ans is True:
    print("AC")
else:
    print("WA")


    
