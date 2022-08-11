# dfs, bfs
# 시간초과 문제가 발생했는데, input() 을 sys.stdin.readline()으로 바꾸어주니 해결되었다.
import sys
sys.setrecursionlimit(100000)


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def main():
    n, m = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    count = 0
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1

    print(count)


main()
