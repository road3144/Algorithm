number = int(input())
cnt = 0

while(number > 0):
    if(number >= 15 or number%5 == 0):
        number = number - 5
        cnt = cnt + 1
    else:
        number = number - 3
        cnt = cnt + 1
if (number != 0):
    cnt = -1
print(cnt)
