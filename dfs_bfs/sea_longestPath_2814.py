def dfs(v):
    global answer
    global max_answer
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            answer += 1
            dfs(i)
            visited[i] = False
            answer -= 1
        else:
            max_answer = max(max_answer, answer)


T = int(input())
for test_case in range(1, T + 1):
    max_answer = 1
    answer = 1
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for a in range(1, n+1):
        visited = [False] * (n + 1)
        answer = 1
        visited[a] = True
        dfs(a)
    print('#' + str(test_case), max_answer)


