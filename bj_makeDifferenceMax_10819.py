n = int(input())
data = list(map(int, input().split()))
data.sort()

data1 = data[:n//2]
data1.reverse()
data2 = data[n//2 + (n % 2):]
mid = data[n//2]
if n % 2 == 0:
    ans = (sum(data2) * 2 - data2[0]) - (sum(data1) * 2 - data1[0])
else:
    if data2[0] - mid > mid - data1[0]:
        ans = (sum(data2) * 2) - (sum(data1) * 2 - data1[0] + mid)
    else:
        ans = (sum(data2) * 2 - data2[0] + mid) - (sum(data1) * 2)
print(ans)
