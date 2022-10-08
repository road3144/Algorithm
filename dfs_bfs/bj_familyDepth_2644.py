import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, start, visited, goal):
    queue = deque()
    queue.append((start, 0))
    depth = -1
    while queue:
        v, depth = queue.popleft()
        if v == goal:
            return depth
        for i in graph[v]:
            if not visited[i]:
                queue.append((i, depth+1))
                visited[i] = True
    return -1



n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(graph, a, visited, b))
