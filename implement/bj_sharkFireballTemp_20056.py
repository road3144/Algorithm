import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
fireballs = []

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(m):
    fireballs.append(list(map(int, input().split())))
for fire in fireballs:
    fire[0] -= 1
    fire[1] -= 1


def union_balls(targets_map):
    for k, targets in targets_map.items():
        cnt = len(targets)
        if not targets:
            return
        tot_m = 0
        tot_s = 0
        tot_d = 0
        pop_cnt = 0
        nr, nc = k
        for i in targets:
            idx = i - 1
            tot_m += fireballs[idx][2]
            tot_s += fireballs[idx][3]
            tot_d += fireballs[idx][4] % 2
        if tot_d % cnt == 0:
            direct = 0
        else:
            direct = 1

        if tot_m // 5 >= 1:
            for i in range(4):
                new_fire = [nr, nc, tot_m // 5, tot_s // cnt, i * 2 + direct]
                fireballs.append(new_fire)

    for targets in targets_map.values():
        for i in targets:
            idx = i - 1 - pop_cnt
            fireballs.pop(idx)
            pop_cnt += 1




for j in range(k):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    targets_map = dict()
    for i in range(1, len(fireballs) + 1):
        r, c, m, s, d = fireballs[i-1]
        nr = (r + dx[d] * s) % n
        nc = (c + dy[d] * s) % n
        fireballs[i - 1][0] = nr
        fireballs[i - 1][1] = nc
        if graph[nr][nc] == 0:
            graph[nr][nc] = i
        else:
            if (nr, nc) in targets_map.keys():
                targets_map[(nr, nc)].append(i)
            else:
                targets_map[(nr, nc)] = [graph[nr][nc], i]

    for fire in fireballs:
        print(fire)
    print("++++++++++++")
    union_balls(targets_map)
    for fire in fireballs:
        print(fire)
    print("=================")
ans = 0
for fire in fireballs:
    ans += fire[2]
print(ans)