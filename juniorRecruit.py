t = int(input())
ans = []
for i in range(t):
    n = int(input())
    cnt = 0
    grd = []
    for j in range(n):
        grd.append(list(map(int, input().split())))
    grd.sort()
    mi = n
    for j in range(n):
        if grd[j][1] > mi:
            cnt += 1
        else:
            mi = grd[j][1]
    ans.append(n-cnt)
for i in ans:
    print(i)