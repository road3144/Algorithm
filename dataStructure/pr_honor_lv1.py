from queue import PriorityQueue


def solution(k, score):
    answer = []
    q = PriorityQueue()
    for i in range(len(score)):
        q.put(score[i])
        if i > k-1:
            q.get()
        ans = q.get()
        answer.append(ans)
        q.put(ans)
    return answer
