n = int(input())
a_l = list(map(int, input().split()))
m = int(input())
q_l = list(map(int, input().split()))

for q in q_l:
    flag = False
    for i in range(1 << len(a_l)):
        s = 0
        for j in range(len(a_l)):
            if (i >> j) & 1 == 1:
                s += a_l[j]
        if q == s:
            flag = True
            print("yes")
    if not flag:
        print("no")

        




    


