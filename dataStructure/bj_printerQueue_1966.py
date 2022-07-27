import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))
    doc = deque([i for i in range(n)])
    rank = 0
    while queue:
        order = queue.popleft()
        temp = doc.popleft()
        if not queue or order >= max(queue):
            rank += 1
            if temp == m:
                break
        else:
            queue.append(order)
            doc.append(temp)
    print(rank)


