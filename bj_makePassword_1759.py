from itertools import combinations

l, c = map(int, input().split())
data = list(input().split())
data.sort()
vowel = []
consonant = []

for i in data:
    if i in 'aeiou':
        vowel.append(i)
    else:
        consonant.append(i)

ans = []
password = list(combinations(data, l))
for i in password:
    vCnt = 0
    cCnt = 0
    for j in i:
        if j in vowel:
            vCnt += 1
        elif j in consonant:
            cCnt += 1
    if vCnt >= 1 and cCnt >= 2:
        ans.append(''.join(i))

for i in ans:
    print(i)
