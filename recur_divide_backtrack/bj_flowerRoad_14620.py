import sys

input = sys.stdin.readline

n = int(input())
graph = []
answer = int(1e9)
s = []
temp = [[0 for _ in range(n)]for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))


def is_not_meeting(i, j):
    if temp[i][j] >= 1 or temp[i-1][j] >= 1 or temp[i][j-1] >= 1 or temp[i+1][j] >= 1 or temp[i][j+1] >= 1:
        return False
    return True


def dfs():
    global answer
    if len(s) == 3:
        total = 0
        for x, y in s:
            total += graph[x][y] + graph[x-1][y] + graph[x][y-1] + graph[x+1][y] + graph[x][y+1]
        answer = min(answer, total)
        return
    for i in range(1, n-1):
        for j in range(1, n-1):
            if (i, j) not in s and is_not_meeting(i, j):
                temp[i][j] += 1
                temp[i - 1][j] += 1
                temp[i][j - 1] += 1
                temp[i + 1][j] += 1
                temp[i][j + 1] += 1
                s.append((i, j))
                dfs()
                x, y = s.pop()
                temp[x][y] -= 1
                temp[x - 1][y] -= 1
                temp[x][y - 1] -= 1
                temp[x + 1][y] -= 1
                temp[x][y + 1] -= 1


dfs()
print(answer)