from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()


def push(item):
    queue.append(item)


def pop():
    if empty() == 0:
        return queue.popleft()
    else:
        return -1


def size():
    return len(queue)


def empty():
    if len(queue) == 0:
        return 1
    else:
        return 0


def front():
    if empty() == 0:
        return queue[0]
    else:
        return -1


def back():
    if empty() == 0:
        return queue[size() - 1]
    else:
        return -1


for _ in range(n):
    args = input().split()
    commend = args[0].strip()
    if len(args) >= 2:
        item = args[1].strip()
    if commend == 'push':
        push(item)
    if commend == 'pop':
        print(pop())
    if commend == 'size':
        print(size())
    if commend == 'empty':
        print(empty())
    if commend == 'front':
        print(front())
    if commend == 'back':
        print(back())

