import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
ans = []

for _ in range(t):
    commands = list(input().rstrip())
    n = int(input())
    is_error = False
    direct = 0
    if n != 0:
        arr = list(map(int, input().replace('[', '').replace(']', '').split(',')))
    else:
        input()
        arr = []
    stack = deque(arr)
    for i in commands:
        if i == 'R':
            direct = (direct + 1) % 2
        if i == 'D':
            if len(stack) == 0:
                ans.append('error')
                is_error = True
                break
            if direct == 0:
                stack.popleft()
            if direct == 1:
                stack.pop()
    if is_error:
        continue
    if direct == 0:
        ans.append(str(list(stack)).replace(' ', ''))
    else:
        stack.reverse()
        ans.append(str(list(stack)).replace(' ', ''))

for i in ans:
    print(i)
