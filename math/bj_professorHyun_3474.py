import sys

input = sys.stdin.readline

t = int(input())
answers = []

for _ in range(t):
    n = int(input())
    divisor = 5
    answer = 0
    while divisor <= n:
        answer += n // divisor
        divisor *= 5
    answers.append(answer)

for answer in answers:
    print(answer)
