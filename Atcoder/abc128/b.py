n = int(input())
rests = []
for i in range(n):
    rest_name, point = input().split() 
    rests.append([rest_name, int(point)])

sorted_rests = sorted(rests, key=lambda x: (x[0], -x[1]))

for i in range(len(sorted_rests)):
    for j in range(len(rests)):
        if sorted_rests[i] == rests[j]:
            print(j + 1)
            break
            
