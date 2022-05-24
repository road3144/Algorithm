n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x, y, direc = map(int, input().split())
d[x][y] = 1

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direc
    direc -= 1
    if direc == -1:
        direc = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direc]
    ny = y + dy[direc]

    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direc]
        ny = y - dy[direc]
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
