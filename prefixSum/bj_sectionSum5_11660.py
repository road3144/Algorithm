import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
sums = [[0 for _ in range(n+1)] for _ in range(n+1)]
ans = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
for i in range(1, n+1):
    for j in range(1, n+1):
        sums[i][j] = sums[i][j-1] + sums[i-1][j] - sums[i-1][j-1] + arr[i-1][j-1]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans.append(sums[x2][y2] - sums[x2][y1-1] - sums[x1-1][y2] + sums[x1-1][y1-1])
for i in ans:
    print(i)
