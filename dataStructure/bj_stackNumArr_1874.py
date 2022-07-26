import sys
input = sys.stdin.readline

n = int(input())
data = [i for i in range(n, 0, -1)]
stack = []
answer = []
operator = []

for i in range(n):
    answer.append(int(input()))
answer.reverse()
while data:
    stack.append(data.pop())
    operator.append('+')
    while stack[len(stack) - 1] == answer[len(answer) - 1]:
        stack.pop()
        answer.pop()
        operator.append('-')
        if not stack or not answer:
            break

if not stack and not answer:
    for i in range(len(stack)):
        operator.append('-')
    for i in operator:
        print(i)
else:
    print('NO')
