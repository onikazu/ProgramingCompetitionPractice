n = int(input())
trans = [int(input()) for _ in range(5)]

people = [n, 0, 0, 0, 0, 0]
cnt = 0

while people[5] < n:
    for i in reversed(range(0, len(trans))):
        if people[i] >= trans[i]:
            people[i] -= trans[i]
            people[i+1] += trans[i]
        else:
            people[i + 1] += people[i]
            people[i] = 0
    cnt += 1
print(cnt)
    
