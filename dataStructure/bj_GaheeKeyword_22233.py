import sys

input = sys.stdin.readline

n, m = map(int, input().split())

memo = set()

for _ in range(n):
    memo.add(str(input().rstrip()))

for _ in range(m):
    keywords = list(map(str, input().rstrip().split(',')))
    for keyword in keywords:
        if keyword in memo:
            memo.remove(keyword)
    print(len(memo))
