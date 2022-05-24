n, k = map(int, input().split())
data = list()
for i in range(n):
    data.append(int(input()))
cnt = 0
data.reverse()
for i in data:
    if k >= i:
        cnt = cnt + (k // i)
        k = k % i
        if k == 0:
            break
print(cnt)