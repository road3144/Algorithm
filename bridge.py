from math import factorial

number = int(input())
n = list()
m = list()
def mcn(n,m):
    cnt = factorial(m)//(factorial(n)*factorial(m-n))
    return cnt
for i in range(1,number+1):
    tmp = input()
    n.append(int(tmp.split(' ')[0]))
    m.append(int(tmp.split(' ')[1]))

for i in range(0,number):
    print(mcn(n[i],m[i]))
