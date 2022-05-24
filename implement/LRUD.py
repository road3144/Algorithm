n = int(input())
plan = list(input().split())

x = 1
y = 1

for i in range(len(plan)):
    if(plan[i] == 'L' and y != 1):
        y -= 1
    elif (plan[i] == 'R' and y != n):
        y += 1
    elif (plan[i] == 'U' and x != 1):
        x -= 1
    elif (plan[i] == 'D' and x != n):
        x += 1

print(x, y)