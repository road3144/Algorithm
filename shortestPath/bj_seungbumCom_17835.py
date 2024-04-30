# 시간초과 나와서 다른 풀이 참고, 그래프 역방향 저장, 출발지 여러개일때 큐에 한번에 넣기
import sys
import heapq

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = float('inf')

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))

inter = list(map(int, input().split()))
min_dist = [INF] * (n+1)
distance = [INF] * (n + 1)


def dijkstra():
    q = []
    for i in inter:
        distance[i] = 0
        heapq.heappush(q, (0, i))

    while q:
        now_cost, now_node = heapq.heappop(q)
        if distance[now_node] < now_cost:
            continue
        for next_node, cost in graph[now_node]:
            next_cost = now_cost + cost
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(q, (next_cost, next_node))


dijkstra()
index = 1
answer = 0
for i in range(1, n+1):
    if answer < distance[i]:
        index = i
        answer = distance[i]

print(index)
print(answer)
