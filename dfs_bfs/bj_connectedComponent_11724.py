import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[]for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(graph, visited, start, cnt):
    queue = deque()
    queue.append(start)
    visited[start] = cnt
    while queue:
        nv = queue.popleft()
        for i in graph[nv]:
            if visited[i] == 0:
                visited[i] = cnt
                queue.append(i)


cnt = 1
for i in range(1, n+1):
    if visited[i] == 0:
        bfs(graph, visited, i, cnt)
        cnt = cnt + 1

print(max(visited))
