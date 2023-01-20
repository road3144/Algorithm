import sys
input = sys.stdin.readline

n = int(input())
data = []
start = []
link = []
minDiff = int(1e9)

for _ in range(n):
    data.append(list(map(int, input().split())))


def dfs(k):
    global minDiff
    startSum = 0
    linkSum = 0
    if k == n // 2:
        for i in range(n):
            if i not in start:
                link.append(i)
        for i in range(0, n//2 - 1):
            for j in range(i+1, n//2):
                startSum += data[start[i]][start[j]] + data[start[j]][start[i]]
                linkSum += data[link[i]][link[j]] + data[link[j]][link[i]]
        diff = abs(startSum - linkSum)
        link.clear()
        if minDiff > diff:
            minDiff = diff
        return
    for i in range(n):
        if (i not in start) and (len(start) == 0 or start[-1] < i):
            start.append(i)
            dfs(k+1)
            start.pop()


dfs(0)
print(minDiff)
