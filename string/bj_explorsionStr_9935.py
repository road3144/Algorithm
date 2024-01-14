import sys

input = sys.stdin.readline

data = list(input().rstrip())
boom = input().rstrip()
bo_size = len(boom)

stack = []
for i in range(len(data)):
    stack.append(data[i])
    if ''.join(stack[-bo_size:]) == boom:
        for _ in range(bo_size):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
