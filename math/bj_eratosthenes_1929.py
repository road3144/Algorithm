import sys

input = sys.stdin.readline

n, m = map(int, input().split())
end = 1000000
ans = [False, False] + [True] * (end-1)


for i in range(2, 1000001):
    if ans[i]:
        for j in range(i*2, end, i):
            ans[j] = False

for i in range(n, m+1):
    if ans[i]:
        print(i)
