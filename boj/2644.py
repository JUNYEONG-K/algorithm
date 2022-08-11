# bfs
from collections import deque


def main():
    n = int(input())  # 전체 사람 수
    x, y = map(int, input().split())
    m = int(input())  # 간선 수

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    check = [0] * (n+1)

    bfs(graph, x, check)

    print(check[y] if check[y] > 0 else -1)


def bfs(graph, start, check):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if check[i] == 0:
                queue.append(i)
                check[i] = check[v] + 1


def dfs(graph, start, check):
    for i in graph[start]:
        if check[i] == 0:
            check[i] = check[start] + 1
            dfs(graph, start, check)


main()
