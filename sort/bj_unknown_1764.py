import sys

input = sys.stdin.readline

n, m = map(int, input().split())
hearList = []
seeList = []

for i in range(n):
    hearList.append(input().rstrip())
for i in range(m):
    seeList.append(input().rstrip())

unknownList = list(set(hearList) & set(seeList))
unknownList.sort()
print(len(unknownList))
for i in unknownList:
    print(i)
