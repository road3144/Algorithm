from collections import deque

n = int(input())
dummy = [[0 for _ in range(n)] for _ in range(n)]
k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    dummy[r - 1][c - 1] = 1
mc = int(input())
moving = deque()
for i in range(mc):
    x, c = input().split()
    moving.append((int(x), c))
count = 0
hr = hc = 0
snake = deque([(hr, hc)])
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
direct = 0


def turn_direct(c, direct):
    if c == 'L':
        return (direct + 3) % 4
    else:
        return (direct + 1) % 4


while True:
    count += 1

    hr = hr + dr[direct]
    hc = hc + dc[direct]

    if hr < 0 or hr >= n or hc < 0 or hc >= n:
        break
    if (hr, hc) in snake:
        break

    snake.append((hr, hc))
    if dummy[hr][hc] == 1:
        dummy[hr][hc] = 0
    else:
        snake.popleft()

    if moving:
        x, c = moving.popleft()
        if x == count:
            direct = turn_direct(c, direct)
        else:
            moving.appendleft((x, c))

print(count)

# 처음에 사과를 먹었을 때 사과가 없어지는 로직을 작성하지 않아 틀림처리 이후 수정