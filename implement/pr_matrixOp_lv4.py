# 답 보고 아이디어 획듣
from collections import deque


def solution(rc, operations):
    answer = []
    n, m = len(rc), len(rc[0])

    rows = deque()
    for row in rc:
        rows.append(deque(row[1:-1]))
    cols = [deque(rc[r][0] for r in range(n)), deque(rc[r][m-1] for r in range(n))]

    for op in operations:
        if op == 'ShiftRow':
            rows.appendleft(rows.pop())
            cols[0].appendleft(cols[0].pop())
            cols[1].appendleft(cols[1].pop())
        else:
            rows[n-1].append(cols[1].pop())
            cols[0].append(rows[n-1].popleft())
            rows[0].appendleft(cols[0].popleft())
            cols[1].appendleft(rows[0].pop())
    for r in range(n):
        answer.append([])
        answer[r].append(cols[0][r])
        answer[r].extend(rows[r])
        answer[r].append((cols[1][r]))
    return answer


rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
operations = ["Rotate", "ShiftRow"]
print(solution(rc, operations))
