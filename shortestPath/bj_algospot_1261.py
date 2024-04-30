import sys
import heapq

input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append((list(map(int, input().rstrip()))))

INF = int(1e9)
distance = [[INF for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dijkstra():
    q = []
    distance[0][0] = 0
    heapq.heappush(q, (graph[0][0], 0, 0))

    while q:
        now_cost, x, y = heapq.heappop(q)
        for i in range(4):
            nx, ny = (x + dx[i], y + dy[i])
            if 0 <= nx < n and 0 <= ny < m:
                new_cost = now_cost + graph[nx][ny]
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))


dijkstra()
print(distance[n-1][m-1])
