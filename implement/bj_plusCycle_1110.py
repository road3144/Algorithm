n = int(input())
newNum = 0
cnt = 0

fir = n // 10
sec = n % 10
pNum = fir + sec
newNum = (sec * 10) + (pNum % 10)
cnt += 1
while n != newNum:
    fir = newNum // 10
    sec = newNum % 10
    pNum = fir + sec
    newNum = (sec * 10) + (pNum % 10)
    cnt += 1

print(cnt)
