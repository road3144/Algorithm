import sys

input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []
players = []
player_lv = dict()

for _ in range(p):
    data = input().split()
    lv = int(data[0])
    nick = data[1]
    player_lv[nick] = lv

    if not rooms:
        rooms.append(lv-10)
        players.append([nick])
        continue
    is_find = False
    for i in range(len(rooms)):
        if rooms[i] <= lv <= rooms[i] + 20 and len(players[i]) < m:
            players[i].append(nick)
            is_find = True
            break
    if not is_find:
        rooms.append(lv-10)
        players.append([nick])

for i in range(len(rooms)):
    players[i].sort()
    if len(players[i]) < m:
        print("Waiting!")
    else:
        print("Started!")
    for nick in players[i]:
        print(player_lv[nick], end=" ")
        print(nick)
