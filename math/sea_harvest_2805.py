T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))

    answer = 0
    for i in range(n//2):
        answer += sum(graph[i][n//2-i:n//2+i+1])
        answer += sum(graph[n-i-1][n//2-i:n//2+i+1])
    answer += sum(graph[n//2])
    print('#' + str(test_case), answer)

