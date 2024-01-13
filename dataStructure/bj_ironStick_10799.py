import sys

input = sys.stdin.readline

raw = list(input().rstrip())

stack = []
answer = 0
for i in range(len(raw)):
    if raw[i] == '(':
        stack.append('(')
    else:
        if raw[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
print(answer)
