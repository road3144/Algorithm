n = int(input())
data = list()
for i in range(n):
    data.append(list(map(int, input().split())))
cnt = 0

data.sort(key=lambda x: (x[1], x[0]))
end = 0
for i in data:
    if i[0] >= end:
        end = i[1]
        cnt = cnt + 1

print(cnt)
