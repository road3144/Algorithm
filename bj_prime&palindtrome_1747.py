n = int(input())


def prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def palindrome(num):
    numList = list(map(int, str(num)))
    newNum = 0
    cnt = 1
    for i in numList:
        newNum += i * cnt
        cnt *= 10
    if num == newNum:
        return True
    else:
        return False


while True:
    if palindrome(n):
        if prime(n):
            break
        else:
            n += 1
    else:
        n += 1
print(n)
