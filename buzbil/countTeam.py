from math import factorial
n = int(input())
skills = []
for i in range(n):
    skills.append(int(input()))
minPlayers = int(input())
minLevel = int(input())
maxLevel = int(input())

print(skills)
def countTeam(skills, minPlayers, minLevel, maxLevel):
    sk = []
    for j in skills:
        if j >= minLevel and j <= maxLevel:
            sk.append(j)
    print(sk)
    maxPlayer = len(sk)
    cnt = 0
    for j in range(minPlayers, maxPlayer + 1):
        cnt += factorial(maxPlayer) // (factorial(j) * factorial(maxPlayer - j))
    return cnt


print(countTeam(skills, minPlayers, minLevel, maxLevel))
