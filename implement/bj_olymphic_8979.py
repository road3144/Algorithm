n, k = map(int, input().split())
grade = []
rank = 1

for i in range(n):
    grade.append(list(map(int, input().split())))

kGrade = []

for i in grade:
    if i[0] == k:
        kGrade = i

for i in grade:
    if i[1] > kGrade[1]:
        rank = rank + 1
    if i[1] == kGrade[1] and i[2] > kGrade[2]:
        rank = rank + 1
    elif i[1] == kGrade[1] and i[2] == kGrade[2] and i[3] > kGrade[3]:
        rank = rank + 1

print(rank)
