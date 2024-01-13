import sys
import heapq

input = sys.stdin.readline

n, d = map(int, input().split())
road = [[(1, i+1)] for i in range(d+1)]
distance = [int(1e9)] * (d+1)
for _ in range(n):
    start, ter, cost = map(int, input().split())
    if ter > d or cost > ter - start:
        continue
    road[start].append((cost, ter))

start = 0


def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for nex_cost, nex_node in road[now]:
            total = dist + nex_cost
            if 0 <= nex_node <= d and total < distance[nex_node]:
                distance[nex_node] = total
                heapq.heappush(q, (total, nex_node))


dijkstra(start)

print(distance[d])
