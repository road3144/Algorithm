import sys
input = sys.stdin.readline

n, k = map(int, input().split())

data = [False, False] + [True] * (n-1)
cnt = 0

for i in range(2, n+1):
    if data[i]:
        data[i] = False
        cnt += 1
        if cnt == k:
            print(i)
            break
        for j in range(i*2, n+1, i):
            if data[j]:
                data[j] = False
                cnt += 1
            if cnt == k:
                print(j)
                exit(0)
