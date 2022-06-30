import sys
input = sys.stdin.readline

n = int(input())
data = [0] * 10001
for _ in range(n):
    data[int(input())] += 1
for i in range(10001):
    if data[i] != 0:
        for _ in range(data[i]):
            print(i)
