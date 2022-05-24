import re

s = input()
data = re.split('[+-]', s)

for i in data:
    s = s.replace(i, i.lstrip("0"), 1)

s = '(' + s + ')'
cnt = 0

for i in s:
    if i == '-':
        cnt = cnt + 1

s = s.replace("-", ")-(", cnt)
print(eval(s))