colorDic = {'R': [], 'B': [], 'Y': [], 'G': []}
score = 0
numDic = {id: 0 for id in range(1, 10)}
pair = []
tri = []
for i in range(5):
    color, num = input().split()
    colorDic[color].append(int(num))
    numDic[int(num)] = numDic[int(num)] + 1

for i in range(1, 10):
    if numDic[i] == 0:
        del numDic[i]

if len(numDic.keys()) == 5:
    score = max(numDic.keys()) + 100
    if (max(numDic.keys()) - min(numDic.keys())) == 4:
        score = max(numDic.keys()) + 500
else:
    for k in numDic:
        if numDic[k] == 4:
            score = k + 800
        if numDic[k] == 3:
            score = k + 400
            tri.append(k)
        if numDic[k] == 2:
            score = k + 200
            pair.append(k)
        if len(pair) == 2:
            score = pair[1]*10 + pair[0] + 300
        if len(pair) == 1 and len(tri) == 1:
            score = tri[0]*10 + pair[0] + 700

for k in colorDic:
    if len(colorDic[k]) == 5:
        score = colorDic[k][4] + 600
        colorDic[k].sort()
        if(colorDic[k][4] - colorDic[k][0]) == 4:
            score = colorDic[k][4] + 900

print(score)
