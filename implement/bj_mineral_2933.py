from collections import deque
import copy
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
cave = []
for _ in range(r):
    cave.append(list(input()))
n = int(input())
heights = list(map(int, input().split()))
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def print_cave(cave):
    for i in cave:
        for j in i:
            print(j, end='')


def make_cluster(cave, mineral, visited):
    queue = deque()
    queue.append(mineral)
    cluster = []
    while queue:
        i, j = queue.popleft()
        visited[i][j] = 'v'
        cluster.append((i, j))
        for d in range(4):
            ni = i + dr[d]
            nj = j + dc[d]
            if ni < 0 or ni >= r or nj < 0 or nj >= c:
                continue
            if visited[ni][nj] == 'v':
                continue
            if cave[ni][nj] == 'x':
                visited[ni][nj] = 'v'
                queue.append((ni, nj))
    cluster.sort(key = lambda x : (-x[0], x[1]))
    return cluster


def is_droppable(cave, cluster):
    bottom = 0
    for mineral in cluster:
        i, j = mineral
        bottom = max(i, bottom)
        if i == r-1:
            return False
        if (i+1, j) not in cluster and cave[i+1][j] == 'x':
            return False
    return True


def drop(cave):
    visited = copy.deepcopy(cave)
    clusters = []
    for i in range(r):
        for j in range(c):
            if cave[i][j] == 'x' and visited[i][j] != 'v':
                mineral = (i, j)
                clusters.append(make_cluster(cave, mineral, visited))

    for cluster in clusters:
        while is_droppable(cave, cluster):
            copy_cluster = []
            for mineral in cluster:
                i, j = mineral
                if cave[i+1][j] == '.':
                    cave[i][j] = '.'
                    cave[i+1][j] = 'x'
                    copy_cluster.append((i+1, j))
            cluster = copy_cluster


for i in range(n):
    height = r - heights[i]
    t = 0
    if i % 2 == 0:
        for j in range(c):
            if cave[height][j] == 'x':
                cave[height][j] = '.'
                t = 1
                break
    else:
        for j in range(c-1, -1, -1):
            if cave[height][j] == 'x':
                cave[height][j] = '.'
                t = 1
                break
    if t == 1:
        drop(cave)

print_cave(cave)



