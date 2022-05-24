n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))
result = 0

for i in range(len(price) - 1):
    if price[i] <= price[i+1]:
        price[i+1] = price[i]

for i in range(len(dis)):
    result = result + (dis[i] * price[i])

print(result)