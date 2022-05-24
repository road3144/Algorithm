import sys

input = sys.stdin.readline

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

v = 2

def apartNum(x, y, v):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = v
        apartNum(x - 1, y, v)
        apartNum(x + 1, y, v)
        apartNum(x, y + 1, v)
        apartNum(x, y - 1, v)
        return True
    return False


for i in range(n):
    for j in range(n):
        if apartNum(i, j, v):
            v = v + 1
            apartNum(i, j, v)


v = v-1
part = [0] * (v-1)
for i in range(v-1):
    for j in range(n):
        part[i] = part[i] + graph[j].count(i+2)

part.sort()
print(v-1)
for i in part:
    print(i)

