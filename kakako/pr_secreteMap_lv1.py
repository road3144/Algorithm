def solution(n, arr1, arr2):
    answer = [str("") for i in range(n)]
    arr3 = []
    for i in range(n):
        arr3.append(int(arr1[i] | arr2[i]))
    for i in range(n):
        for j in range(n-1, -1, -1):
            k = 2 ** j
            if arr3[i] >= k:
                answer[i] += "#"
                arr3[i] -= k
            else:
                answer[i] += " "
    return answer


n = 6
arr1 = [46, 33, 33,22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))
