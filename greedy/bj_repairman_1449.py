n, l = map(int, input().split())
hole = list(map(int, input().split()))
hole.sort()
pipe = [0] * 1001
cnt = 0
for i in hole:
    pipe[i] = 1
for i in range(1, 1001):
    if pipe[i] == 1 and pipe[i] != 2:
        for j in range(l):
            if (i+j) <= 1000:
                pipe[i+j] = 2
        cnt += 1

print(cnt)
