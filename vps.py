number = int(input())
ps = []
vps = []
for i in range(number):
    ps.append(input())

for p in ps:
    x = 0
    y = 0
    for ch in p:
        if(ch == '('):
            x = x + 1
        if (ch == ')'):
            y = y + 1
            if(y > x):
                vps.append("NO")
                break
    if(x == y):
        vps.append("YES")
    elif(x > y):
        vps.append("NO")


for p in vps:
    print(p)