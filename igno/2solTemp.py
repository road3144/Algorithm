from collections import deque

def move_element(large, small):
    small.append(large[0])
    large.popleft()


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    total = sum(queue1) + sum(queue2)
    avg = total // 2
    if total % 2 == 1:
        return -1
    if max(queue1) > avg or max(queue2) > avg:
        return 1
    while sum(queue1) != avg and queue1 and queue2 and answer < (len(queue1) * 2):
        answer += 1
        if sum(queue1) < avg:
            move_element(queue2, queue1)
        else:
            move_element(queue1, queue2)
    if not queue1 or not queue2:
        return -1
    return answer


queue1 = [1, 1]
queue2 = [1, 5]
print(solution(queue1, queue2))

def find(queue, avg):
    for i in range(len(queue)):
        for j in range(len(queue) - 1, i-1, -1):
            if sum(queue[i:j+1]) == avg:
                return i, j
    return 0, 0


def solution(queue1, queue2):
    answer = 0
    total_queue = queue1 + queue2
    start = 0
    end = len(queue1) -1
    total = sum(total_queue)
    avg = total // 2
    if total % 2 == 1:
        return -1
    if max(queue1) > avg or max(queue2) > avg:
        return -1
    i, j = find(total_queue, avg)
    answer += abs(i - start)
    answer += abs(j - end)

    return answer


queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]
print(solution(queue1, queue2))

# elif max(total_queue) == avg:
# idx = total_queue.index(max(total_queue))
# answer += abs(start - idx)
# answer += abs(end - idx)
# return answer