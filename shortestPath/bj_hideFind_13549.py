# dp 인줄 알고 풀었으나 아니였고 검색해서 다익스트라로 제출
import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
INF = int(1e9)
distance = [INF] * 100001


def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for nex_dist, nex_node in [(dist, now*2), (dist+1, now+1), (dist+1, now-1)]:
            if 0 <= nex_node <= 100000 and nex_dist < distance[nex_node]:
                distance[nex_node] = nex_dist
                heapq.heappush(q, (nex_dist, nex_node))


dijkstra(n)
print(distance[k])
