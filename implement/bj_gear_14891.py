import sys
from collections import deque
input = sys.stdin.readline

gear = {}

for i in range(1, 5):
    gear[i] = deque(map(int, list(input().rstrip())))

n = int(input())
actions = []

for _ in range(n):
    actions.append(list(map(int, input().split())))


def turn_right(target, direction):
    if target > 4 or gear[target-1][2] == gear[target][6]:
        return
    if gear[target-1][2] != gear[target][6]:
        turn_right(target+1, -direction)
        gear[target].rotate(direction)


def turn_left(target, direction):
    if target < 1 or gear[target][2] == gear[target+1][6]:
        return
    if gear[target][2] != gear[target + 1][6]:
        turn_left(target - 1, -direction)
        gear[target].rotate(direction)


for action in actions:
    target, direction = action

    turn_left(target - 1, -direction)
    turn_right(target + 1, -direction)
    gear[target].rotate(direction)

result = 0
for i in range(4):
    result += gear[i+1][0] * (2**i)

print(result)