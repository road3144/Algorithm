n = int(input())
data = list(map(int, input().split()))
data.sort()
for i in range(n):
    if i != 0:
        data[i] = data[i-1] + data[i]
result = sum(data)
print(result)
