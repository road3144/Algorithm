import sys
input = sys.stdin.readline


def push(item):
    stack.append(item)


def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())


def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[len(stack) - 1])


def size():
    print(len(stack))


def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)


n = int(input())
stack = []

for _ in range(n):
    args = input().split()
    commend = args[0]
    if len(args) >= 2:
        item = args[1]
    if commend == 'push':
        push(item)
    elif commend == 'pop':
        pop()
    elif commend == 'size':
        size()
    elif commend == 'empty':
        empty()
    elif commend == 'top':
        top()
