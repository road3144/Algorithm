import sys

input = sys.stdin.readline

raw = list(input().rstrip())


def calculate(raw):
    stack = []
    answer = 0
    tmp = 1
    for i in range(len(raw)):
        if raw[i] == '(':
            tmp *= 2
            stack.append(raw[i])
        elif raw[i] == '[':
            tmp *= 3
            stack.append(raw[i])
        elif raw[i] == ')':
            if not stack or stack[-1] != '(':
                return 0
            if raw[i-1] == '(':
                answer += tmp
            stack.pop()
            tmp //= 2
        else:
            if not stack or stack[-1] != '[':
                return 0
            if raw[i-1] == '[':
                answer += tmp
            stack.pop()
            tmp //= 3
    if stack:
        return 0
    return answer


print(calculate(raw))
