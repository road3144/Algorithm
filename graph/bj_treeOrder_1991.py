from string import ascii_uppercase

n = int(input())
UpperAlpha = list(ascii_uppercase)
graph = {id: [] for id in UpperAlpha[:n]}

for i in range(n):
    root, lc, rc = input().split()
    graph[root].append(lc)
    graph[root].append(rc)


def preorder(graph, node):
    if node == '.':
        return
    print(node, end='')
    preorder(graph, graph[node][0])
    preorder(graph, graph[node][1])


def inorder(graph, node):
    if node == '.':
        return
    inorder(graph, graph[node][0])
    print(node, end='')
    inorder(graph, graph[node][1])


def postorder(graph, node):
    if node == '.':
        return
    postorder(graph, graph[node][0])
    postorder(graph, graph[node][1])
    print(node, end='')


preorder(graph, 'A')
print()
inorder(graph, 'A')
print()
postorder(graph, 'A')
