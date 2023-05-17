for test_case in range(1, 10 + 1):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    answer = 0
    for i in range(n):
        is_before_1 = False
        for j in range(n):
            if graph[j][i] == 1:
                is_before_1 = True
            elif graph[j][i] == 2 and is_before_1:
                answer += 1
                is_before_1 = False
    print('#' + str(test_case), answer)