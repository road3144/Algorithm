import sys
input = sys.stdin.readline

n = int(input())
data = []
minAns = int(2e9)
for _ in range(n):
    data.append(list(map(int, input().split())))


def dfs(start, next, value):
    global minAns
    if len(visited) == n:
        if data[next][start] != 0:
            minAns = min(minAns, value + data[next][start])
        return

    for i in range(n):
        if data[next][i] != 0 and i not in visited and value < minAns:
            visited.append(i)
            dfs(start, i, value + data[next][i])
            visited.pop()


for i in range(n):
    visited = [i]
    dfs(i, i, 0)

print(minAns)
