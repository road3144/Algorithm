import sys

input = sys.stdin.readline

n = int(input())
col = [0] * (n + 1)
cnt = 0


def is_promise(i):
    k = 1
    while k < i:
        if col[k] == col[i] or abs(col[k] - col[i]) == abs(k - i):
            return False
        k += 1
    return True


def n_queen(i):
    global cnt
    if is_promise(i):
        if i == n:
            cnt += 1
            return
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queen(i+1)


n_queen(0)
print(cnt)

# pypy3만 통과
