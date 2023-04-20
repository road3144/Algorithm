import sys

input = sys.stdin.readline

n = int(input())
score = [0] * 3
win_time = [0] * 3
last_time = 0
last_team = 0
for _ in range(n):
    temp_team, temp_time = input().split()
    team = int(temp_team)
    minutes, seconds = map(int, temp_time.split(':'))
    time = minutes * 60 + seconds
    score[team] += 1
    win_time[last_team] += time - last_time
    if score[1] > score[2]:
        last_team = 1
    elif score[1] < score[2]:
        last_team = 2
    else:
        last_team = 0
    last_time = time
win_time[last_team] += (48*60) - last_time

print('{0:0>2}:{1:0>2}'.format(str(win_time[1]//60), str(win_time[1]%60)))
print('{0:0>2}:{1:0>2}'.format(str(win_time[2]//60), str(win_time[2]%60)))