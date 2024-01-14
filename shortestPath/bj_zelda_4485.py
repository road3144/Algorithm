import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n:
                new_cost = graph[new_x][new_y] + cost
                if new_cost < distance[new_x][new_y]:
                    distance[new_x][new_y] = new_cost
                    heapq.heappush(q, (new_cost, new_x, new_y))


cnt = 1

while True:
    n = int(input())
    if n == 0:
        break
    graph = []
    distance = [[INF for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    dijkstra()
    print(f"Problem {cnt}: {distance[n-1][n-1]}")
    cnt += 1
