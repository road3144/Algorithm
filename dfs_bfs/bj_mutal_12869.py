import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

n = int(input())
cnt = 0
hp = list(map(int, input().split()))
visited = [[[0 for i in range(61)]for j in range(61)]for k in range(61)]
queue = deque()
queue.append(hp)

if n == 1:
    hp.extend([0, 0])
if n == 2:
    hp.extend([0])
hp.extend([0])
while queue:
    hp = queue.popleft()
    for i in list(map(list, permutations([1, 3, 9], 3))):
        temp = []
        flag = False
        for j in range(3):
            temp.append(max(0, hp[j] - i[j]))
        if sum(temp) == 0:
            print(hp[3] + 1)
            exit(0)
        if not visited[temp[0]][temp[1]][temp[2]]:
            temp.append(hp[3]+1)
            visited[temp[0]][temp[1]][temp[2]] = 1
            queue.append(temp)
# 3차원 dp 시용도 가능
