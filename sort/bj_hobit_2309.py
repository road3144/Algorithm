hobit = []
for i in range(9):
    hobit.append(int(input()))
hobit.sort()
total = sum(hobit)
breaker = 1
for i in range(1, 9):
    for j in range(i):
        if (total - 100) == (hobit[i] + hobit[j]):
            hobit.remove(hobit[i])
            hobit.remove(hobit[j])
            breaker -= 1
            break
    if breaker == 0:
        break

for i in hobit:
    print(i)