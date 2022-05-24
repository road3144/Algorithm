import sys

input = sys.stdin.readline


n, new, p = map(int, input().split())
rank = p + 1
rankList = [0] * p
if n > 0:
    scoreList = list(map(int, input().split()))
    for i in range(len(scoreList)):
        rankList[i] = scoreList[i]

if n == p and new <= min(rankList):
    print(-1)
    exit(0)

for i in rankList:
    if i <= new:
        rank += -1

print(rank)