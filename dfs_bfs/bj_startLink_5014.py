import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
dx = [u, -d]
visited = [0] * (f+1)

queue = deque([s])

while queue:
    x = queue.popleft()
    if x == g:
        print(visited[x])
        exit(0)
    for i in range(2):
        if dx[i] == 0:
            continue
        nx = x + dx[i]
        if nx > f or nx <= 0:
            continue
        if visited[nx] > 0:
            continue
        else:
            visited[nx] = visited[x] + 1
            queue.append(nx)
            if nx == g:
                print(visited[nx])
                exit(0)
print("use the stairs")
