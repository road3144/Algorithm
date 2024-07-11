# 가장 긴 증가하는 부분 수열 문제 이 아이디어를 떠올리는게 포인트 인듯

import sys
input = sys.stdin.readline

n = int(input())
data = [0]
dp = [1] * (n+1)
for _ in range(n):
    data.append(int(input()))

for i in range(1, n+1):
    for j in range(1, i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
