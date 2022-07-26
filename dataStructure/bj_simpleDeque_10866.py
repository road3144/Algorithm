from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()


def push_front(item):
    queue.appendleft(item)


def push_back(item):
    queue.append(item)


def pop_front():
    if empty() == 0:
        return queue.popleft()
    else:
        return -1


def pop_back():
    if empty() == 0:
        return queue.pop()
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
    if commend == 'push_front':
        push_front(item)
    if commend == 'push_back':
        push_back(item)
    if commend == 'pop_front':
        print(pop_front())
    if commend == 'pop_back':
        print(pop_back())
    if commend == 'size':
        print(size())
    if commend == 'empty':
        print(empty())
    if commend == 'front':
        print(front())
    if commend == 'back':
        print(back())

