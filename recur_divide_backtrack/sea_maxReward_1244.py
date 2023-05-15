T = int(input())


def dfs(k):
    global answer
    if k == m:
        temp = ''.join(cards)
        if answer < temp:
            answer = temp
        return
    for i in range(len(str(n))):
        for j in range(i+1, len(str(n))):
            cards[i], cards[j] = cards[j], cards[i]
            temp = ''.join(cards)
            if (temp, k) not in visited:
                visited.add((temp, k))
                dfs(k+1)
            cards[i], cards[j] = cards[j], cards[i]


for test_case in range(1, T + 1):
    n, m = input().rstrip().split()
    answer = '0000000'
    cards = list(n)
    m = int(m)
    visited = set()
    dfs(0)

    print('#' + str(test_case), answer)

