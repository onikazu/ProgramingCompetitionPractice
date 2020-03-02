import heapq

a = [1, 3, 2, 5, 4]
print(a)
heapq.heapify(a)
print(a)

print(heapq.heappop(a))
print(a)

heapq.heappush(a, -2)
print(a)
