import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
result = [0] * n

for i in range(n):
    cnt = data[i]
    for j in range(n):
        if cnt == 0 and result[j] == 0:
            result[j] = i+1
            break
        if result[j] == 0:
           cnt -= 1

print(" ".join(map(str, result)))
