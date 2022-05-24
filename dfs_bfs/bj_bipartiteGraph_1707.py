import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)


def bigra(start, color):
    visited[start] = color

    for i in graph[start]:
        if not visited[i]:
            a = bigra(i, -color)
            if not a:
                return False
        elif visited[i] == visited[start]:
            return False
    return True


for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    res = False

    for i in range(e):
        s, g = map(int, input().split())
        graph[s].append(g)
        graph[g].append(s)

    for i in range(1, v+1):
        if not visited[i]:
            res = bigra(i, 1)
        if not res:
            break

    if res:
        print("YES")
    else:
        print("NO")