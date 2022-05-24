from collections import deque
import copy

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

SHEEP = 0
WOLF = 1


def bfs(filed, info):
    global SHEEP, WOLF

    max_sheep = 0
    queue = deque()
    visited_state = set()
    queue.append((0, 1, 0, [0]))
    visited_state.add((0, 1, 0))

    while queue:
        node, sheep, wolf, visited = queue.popleft()
        max_sheep = max(max_sheep, sheep)
        for next_node in filed[node]:
            next_sheep = sheep
            next_wolf = wolf
            if next_node not in visited and info[next_node] == SHEEP:
                next_sheep += 1
            elif next_node not in visited and info[next_node] == WOLF:
                next_wolf += 1
            if next_sheep <= next_wolf:
                continue

            next_state = (next_node, next_sheep, next_wolf)
            if next_state not in visited_state:
                visited_state.add(next_state)
                copy_visited = copy.deepcopy(visited)
                copy_visited.append(next_node)
                queue.append((next_node, next_sheep, next_wolf, copy_visited))

    return max_sheep


def solution(info, edges):
    answer = 0
    filed = [[] for _ in range(len(info))]
    for edge in edges:
        p, c = edge
        filed[p].append(c)
        filed[c].append(p)

    answer = bfs(filed, info)

    return answer


print(solution(info, edges))
