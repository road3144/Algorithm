import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())
rope = []
ans = 0

for i in range(n):
    rope.append(int(input()))
rope.sort()

for i in range(n):
    ans = max(rope[i] * (n-i), ans)

print(ans)
