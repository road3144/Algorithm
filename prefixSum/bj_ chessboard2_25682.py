import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(list(input().rstrip()))


def minimal(color):
    prefix_sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                value = chess[i][j] != color
            else:
                value = chess[i][j] == color
            prefix_sum[i+1][j+1] = prefix_sum[i+1][j] + prefix_sum[i][j+1] - prefix_sum[i][j] + value

    count = int(1e9)
    for i in range(1, n-k+2):
        for j in range(1, m-k+2):
            count = min(count, prefix_sum[i+k-1][j+k-1] - prefix_sum[i+k-1][j-1] - prefix_sum[i-1][j+k-1] + prefix_sum[i-1][j-1])
    return count


print(min(minimal('B'), minimal('W')))
