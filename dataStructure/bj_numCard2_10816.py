import sys
input = sys.stdin.readline

card = [0] * 20000003
n = int(input())
data = list(map(int, input().split(" ")))
m = int(input())
m_data = list(map(int, input().split(" ")))

for i in data:
    card[i] += 1

for i in m_data:
    print(card[i], end=' ')