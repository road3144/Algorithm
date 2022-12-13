def shift_row(rc, r, c):
    temp = rc[r-1]
    for i in range(r-1, 0, -1):
        rc[i] = rc[i-1]
    rc[0] = temp


def rotate(rc, r, c):
    temp = rc[0][c-1]
    for i in range(r-1):
        rc[i][0] = rc[i+1][0]
    for i in range(c-1):
        rc[r-1][i] = rc[r-1][i+1]
    for i in range(r-1, 0, -1):
        rc[i][c-1] = rc[i-1][c-1]
    for i in range(c-1, 0, -1):
        rc[0][i] = rc[0][i-1]
    rc[0][1] = temp


def solution(rc, operations):
    answer = [[]]
    r = len(rc)
    c = len((rc[0]))
    for operation in operations:
        if operation == "ShiftRow":
            shift_row(rc, r, c)
        else:
            rotate(rc, r, c)
    answer = rc
    return answer


rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
operations = ["Rotate", "ShiftRow"]
print(solution(rc, operations))
# temp1 = rc[0].pop()
# rc[0].insert(0, rc[1][0])
# temp2 = rc[r - 1][0]
# rc[r - 1] = rc[r - 1][1:]
# rc[r - 1].append(rc[r - 2][c - 1])
#
# for i in range(1, r - 1):
#     rc[i][0] = rc[i + 1][0]
#     rc[abs(i - r) - 1][c - 1] = rc[abs(i - r) - 2][c - 1]
# rc[1][c - 1] = temp1
# rc[r - 2][0] = temp2