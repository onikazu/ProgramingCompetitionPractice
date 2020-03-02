"""brute force
import itertools


n = int(input())
jobs = [list(map(int, input().split())) for _ in range(n)]

for pattern in itertools.permutations([i for i in range(n)]):
    t = 0
    flag = True
    for i in pattern:
        t += jobs[i][0]
        if t > jobs[i][1]:
            flag = False
    if flag:
        print("Yes")
        exit()
print("No")
"""
import heapq

n = int(input())
jobs = [list(map(int, input().split()[::-1])) for _ in range(n)]

heapq.heapify(jobs)
t = 0
for i in range(len(jobs)):
    deadline, job_t = heapq.heappop(jobs)
    t += job_t
    if t > deadline:
        print("No")
        exit()
print("Yes")

    









