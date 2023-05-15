for test_case in range(1, 10 + 1):
    n = int(input())
    mat = []
    for _ in range(100):
        mat.append(list(map(int, input().split())))

    answer = 0
    dia_total = 0
    re_dia_total = 0
    for i in range(100):
        col_total = 0
        row_total = 0

        for j in range(100):
            col_total += mat[j][i]
            row_total += mat[i][j]
            if i == j:
                dia_total += mat[i][j]
            if i + j == 99:
                re_dia_total += mat[i][j]
        answer = max(answer, col_total, row_total)
    answer = max(answer, dia_total, re_dia_total)

    print('#' + str(test_case), answer)
