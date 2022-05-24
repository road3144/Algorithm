n, m = map(int, input().split())
ice = []
for i in range(n):
    ice.append(list(map(int, input())))

def icedfs(x, y):
    if x <= -1 or x >= n or y <=-1 or y >= m:
        return False

    if ice[x][y] == 0:
        ice[x][y] = 1
        icedfs(x-1, y)
        icedfs(x, y-1)
        icedfs(x+1, y)
        icedfs(x, y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if icedfs(i, j):
            result += 1
