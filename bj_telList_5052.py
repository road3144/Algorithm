import sys
input = sys.stdin.readline


def is_consistent():
    n = int(input())
    telList = []
    for i in range(n):
        telList.append(input().strip())
    telList.sort()
    for i in range(n-1):
        if telList[i+1].startswith(telList[i]):
            return False
    return True


t = int(input())
for k in range(t):
    if is_consistent():
        print('YES')
    else:
        print('NO')
