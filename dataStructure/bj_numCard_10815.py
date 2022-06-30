import sys
input = sys.stdin.readline

n = int(input())
own = set(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))
result = [0] * m

for i in range(m):
    if data[i] in own:
        result[i] = 1
    print(result[i], end=' ')