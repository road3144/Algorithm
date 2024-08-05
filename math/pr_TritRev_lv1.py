def solution(n):
    answer = 0
    arr = []
    while n > 0:
        arr.append(n % 3)
        n = n // 3
    arr.reverse()
    for i in range(len(arr)):
        answer += (3 ** i) * arr[i]

    return answer
