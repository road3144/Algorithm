import sys

input = sys.stdin.readline

n = int(input())
data = []
answer = 0
for _ in range(n):
    data.append(int(input()))

data.sort()
two = []
for i in range(n):
    for j in range(i, n):
        two.append(data[i] + data[j])

two = set(two)

for k in range(n-1, -1, -1):
    for l in range(k):
        if data[k] - data[l] in two:
            answer = max(answer, data[k])

print(answer)
