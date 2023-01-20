import sys

input = sys.stdin.readline

n, m = map(int, input().split())
hr, hc, direct = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 0
flag = False


def left(direct):
    return (direct + 3) % 4


def back(direct):
    return (direct + 2) % 4


def search_around():
    global hr, hc, direct
    for i in range(4):
        if graph[hr + dr[left(direct)]][hc + dc[left(direct)]] == 0:
            direct = left(direct)
            hr += dr[direct]
            hc += dc[direct]
            return True
        else:
            direct = left(direct)
    return False


while True:
    cnt += 1
    graph[hr][hc] = 2

    while not search_around():
        hr += dr[back(direct)]
        hc += dc[back(direct)]
        if graph[hr][hc] == 1:
            flag = True
            break
    if flag:
        break

print(cnt)
