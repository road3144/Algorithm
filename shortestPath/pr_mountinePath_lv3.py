# 답보고 품 복습 필요 - 다익스트라, 플로이드 워셜 연습

import heapq


def solution(n, paths, gates, summits):

    set_summits = set(summits)
    INF = int(1e9)
    answer = [-1, INF]
    graph = [[] for _ in range(n+1)]
    for path in paths:
        a, b, cost = path
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    pq = []
    distance = [INF] * (n+1)

    for gate in gates:
        heapq.heappush(pq, (gate, 0))
        distance[gate] = 0

    while pq:
        node, intent = heapq.heappop(pq)

        if intent < distance[node] or node in set_summits:
            continue
        for next_node, next_cost in graph[node]:
            next_cost = max(distance[node], next_cost)
            if distance[next_node] > next_cost:
                distance[next_node] = next_cost
                heapq.heappush(pq, (next_node, next_cost))

    for summit in sorted(summits):
        if distance[summit] < answer[1]:
            answer[0] = summit
            answer[1] = distance[summit]
    return answer


n = 7
paths = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
gates = [1]
summits = [2, 3, 4]
print(solution(n, paths, gates, summits))