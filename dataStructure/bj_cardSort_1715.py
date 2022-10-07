import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())
card = PriorityQueue()
ans = 0

for i in range(n):
    size = int(input())
    card.put(size)

for i in range(n-1):
    a = card.get()
    b = card.get()
    ans += a + b
    card.put(a + b)

print(ans)
