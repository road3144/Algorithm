from collections import deque


def solution(food):
    answer = ''
    q = deque([0])
    for i in range(len(food) - 1, 0, -1):
        for j in range(food[i] // 2):
            q.append(i)
            q.appendleft(i)

    answer = ''.join(map(str, q))
    return answer
