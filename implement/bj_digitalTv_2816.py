n = int(input())
channel = []
cursor = 0
button = []
for _ in range(n):
    channel.append(input())


def swap(channel, cursor, move):
    temp = channel[cursor]
    channel[cursor] = channel[cursor+move]
    channel[cursor+move] = temp


while channel[cursor] != 'KBS1':
    cursor = cursor + 1
    button.append(1)
while cursor != 0:
    swap(channel, cursor, -1)
    cursor = cursor - 1
    button.append(4)
while channel[cursor] != 'KBS2':
    cursor = cursor + 1
    button.append(1)
while cursor != 1:
    swap(channel, cursor, -1)
    cursor = cursor - 1
    button.append(4)

for i in button:
    print(i, end='')
