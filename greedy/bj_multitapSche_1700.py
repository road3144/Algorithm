n, k = map(int, input().split())

schedule = list(map(int, input().split()))
dp = [0] * (len(schedule))
multi = []
res = maxI = swap = 0
for i in range(k):
    if schedule[i] in multi:
        continue
    elif len(multi) < n:
        multi.append(schedule[i])
    else:
        for j in range(n):
            if not multi[j] in schedule[i:]:
                swap = j
                break
            elif schedule[i:].index(multi[j]) > maxI:
                maxI = schedule[i:].index(multi[j])
                swap = j
        multi[swap] = schedule[i]
        maxI = swap = 0
        res += 1

print(res)