import heapq


# input values
n, m = list(map(int, input().split()))
A = list(map(lambda x: int(x)*(-1), input().split()))

# use priority queue
heapq.heapify(A)

for _ in range(m):
    tmp_min = heapq.heappop(A)
    heapq.heappush(A, (-1)*(-tmp_min//2))
print(-sum(A))
    
