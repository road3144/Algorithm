import sys

input = sys.stdin.readline

end = 1000000
ans = [False, False] + [True] * (end-1)


for i in range(2, 1000001):
    if ans[i]:
        for j in range(i*2, end, i):
            ans[j] = False


def is_true(n):
    for a in range(1, n+1):
        b = n - a
        if ans[a] and ans[b]:
            print(n, "=", a, "+", b)
            return True
    print("Goldbach's conjecture is wrong.")
    return False


while True:
    n = int(input())
    if n == 0:
        break
    is_true(n)

