n = int(input())
send = []
tornado_position = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    send.append(list(map(int, input().split())))

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
cnt = 0


def tornado(n):
    position = ((n - 1) // 2, (n - 1) // 2)
    tornado_position[(n - 1) // 2][(n - 1) // 2] = 1
    for i in range(1, n, 2):
        for j in range(i):
            position = move_tornado(0, position)
        for j in range(i):
            position = move_tornado(1, position)
        for j in range(i + 1):
            position = move_tornado(2, position)
        for j in range(i + 1):
            position = move_tornado(3, position)
    for i in range(n-1):
        position = move_tornado(0, position)


def move_tornado(direct, position):
    r, c = position
    tornado_position[r][c] = 0
    nr = r + dr[direct]
    nc = c + dc[direct]
    tornado_position[nr][nc] = 1
    position = (nr, nc)
    move_send(direct, position)
    return position


def move_send(direct, position):
    global cnt
    r, c = position
    send_dr, send_dc, send_percent = directed_send(direct)
    position_send = send[r][c]
    for i in range(9):
        nr = r + send_dr[i]
        nc = c + send_dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            cnt += (position_send * send_percent[i]) // 100
            send[r][c] = send[r][c] - ((position_send * send_percent[i]) // 100)
        else:
            send[nr][nc] = send[nr][nc] + ((position_send * send_percent[i]) // 100)
            send[r][c] = send[r][c] - ((position_send * send_percent[i]) // 100)
    nr = r + dr[direct]
    nc = c + dc[direct]
    if nr < 0 or nr >= n or nc < 0 or nc >= n:
        cnt += send[r][c]
        send[r][c] = 0
    else:
        send[nr][nc] = send[nr][nc] + send[r][c]
        send[r][c] = 0


def directed_send(direct):
    send_dr = [1, 1, 1, 2, 0, -1, -1, -1, -2]
    send_dc = [-1, 0, 1, 0, -2, -1, 0, 1, 0]
    send_percent = [10, 7, 1, 2, 5, 10, 7, 1, 2]
    if direct == 0:
        setting = [send_dr, send_dc, send_percent]
        return setting
    elif direct == 1:
        for i in range(9):
            send_dr[i] = send_dr[i] * -1
            send_dc[i] = send_dc[i] * -1
        setting = [send_dc, send_dr, send_percent]
        return setting
    elif direct == 2:
        for i in range(9):
            send_dr[i] = send_dr[i] * -1
            send_dc[i] = send_dc[i] * -1
        setting = [send_dr, send_dc, send_percent]
        return setting
    elif direct == 3:
        setting = [send_dc, send_dr, send_percent]
        return setting


tornado(n)
print(cnt)
