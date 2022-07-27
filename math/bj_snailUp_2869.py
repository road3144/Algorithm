import sys
from collections import deque

input = sys.stdin.readline

a, b, v = map(int, input().split())

answer = (v-a) // (a - b)
temp = v - answer*(a - b)
while temp > 0:
    temp -= a
    answer += 1
    if temp <= 0:
        break
    temp += b
print(answer)
