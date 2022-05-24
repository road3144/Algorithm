n = int(input())
room = []
for _ in range(n):
    room.append(list(input()))

rowCnt = 0
colCnt = 0

for i in room:
    dotCnt = 0
    for j in i:
        if j == '.':
            dotCnt += 1
        else:
            dotCnt = 0
        if dotCnt == 2:
            rowCnt += 1
for i in range(n):
    dotCnt = 0
    for j in range(n):
        if room[j][i] == '.':
            dotCnt += 1
        else:
            dotCnt = 0
        if dotCnt == 2:
            colCnt += 1
print(rowCnt, colCnt)
