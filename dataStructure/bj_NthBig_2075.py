import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    s = list(map(int, input().split()))
    for i in s:
        if len(q) < n:
            heapq.heappush(q, i)
        else:
            if q[0] < i:
                heapq.heappop(q)
                heapq.heappush(q, i)

print(heapq.heappop(q))
