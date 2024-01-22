# 반례 찾으며 해결
import sys
input = sys.stdin.readline

data = list(map(int, input().rstrip()))
dp = [0] * (len(data) + 1)

dp[0] = 1
dp[1] = 1
if data[0] == 0:
    print(0)
    exit(0)

for i in range(2, len(data) + 1):
    if data[i-1] == 0 and 1 <= data[i-2] <= 2:
        dp[i] = (dp[i - 2]) % 1000000
    elif data[i-1] == 0 and (data[i-2] > 2 or data[i-2] < 1):
        print(0)
        exit(0)
    elif (data[i-2] * 10) + data[i-1] <= 26:
        if data[i-2] == 0:
            dp[i] = dp[i-1] % 1000000
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000
    else:
        dp[i] = (dp[i-1]) % 1000000

print(dp[len(data)] % 1000000)
