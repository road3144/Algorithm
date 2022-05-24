n = int(input())
room = list(map(int, input().split()))
b, c = map(int, input().split())

for i in range(n):
    room[i] -= b
cnt = n
for i in room:
    if i >= 0:
        cnt += (i // c)
        if i % c != 0:
            cnt += 1

print(cnt)