import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
data = deque([i for i in range(1, n+1)])
answer = []
for i in range(n):
    cnt = 0
    while cnt != k:
        data.append(data.popleft())
        cnt += 1
    answer.append(data.pop())

print(str(answer).replace('[', '<').replace(']', '>'))