import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())
heap = PriorityQueue()
ans = []

for _ in range(n):
    item = int(input())
    if item == 0:
        if heap.empty():
            ans.append(0)
        else:
            ans.append(heap.get()[1])
    else:
        heap.put((-item, item))
for i in ans:
    print(i)