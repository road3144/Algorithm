def solution(numbers):
    answer = 0
    visited = [True] * 10
    for i in numbers:
        visited[i] = False
    for i in range(10):
        if visited[i]:
            answer += i
    return answer
