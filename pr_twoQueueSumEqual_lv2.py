from collections import deque
from itertools import combinations


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)

    if (sum_queue1 + sum_queue2) % 2 == 1:
        return -1

    while sum_queue1 != sum_queue2:

        if sum_queue1 > sum_queue2:
            item = queue1.popleft()
            queue2.append(item)
            sum_queue1 -= item
            sum_queue2 += item
        else:
            item = queue2.popleft()
            queue1.append(item)
            sum_queue2 -= item
            sum_queue1 += item
        answer += 1
        if not queue1 or not queue2:
            answer = -1
            break
        if answer >= 300001:
            answer = -1
            break
    return answer


queue1 = [1, 1]
queue2 = [1, 5]
print(solution(queue1, queue2))