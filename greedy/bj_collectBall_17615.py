import sys

input = sys.stdin.readline

n = int(input())
balls = str(input().rstrip())
cnt = []

rex = balls.rstrip('R')
cnt.append(rex.count('R'))

rex = balls.rstrip('B')
cnt.append(rex.count('B'))

lex = balls.lstrip('R')
cnt.append(lex.count('R'))

lex = balls.lstrip('B')
cnt.append(lex.count('B'))

print(min(cnt))
