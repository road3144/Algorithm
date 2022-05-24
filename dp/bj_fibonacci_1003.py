n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
dp = list()
dp.append((1, 0))
dp.append((0, 1))
for i in range(2, max(data) + 1):
     dp.append(((dp[i-1][0] + dp[i-2][0]), (dp[i-1][1] + dp[i-2][1])))

for i in data:
    print(dp[i][0], dp[i][1])
