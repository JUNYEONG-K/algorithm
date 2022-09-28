from collections import deque


def dfs(graph, node, visited):
    if not visited[node]:
        visited[node] = True
        for i in graph[node]:
            if not visited[i]:
                dfs(graph, i, visited)
        return True
    return False


def bfs(graph, start_node, visited):
    q = deque([start_node])
    if not visited[start_node]:
        visited[start_node] = True
        while q:
            v = q.popleft()
            for i in graph[v]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
        return True
    return False


def solution(n, computers):
    graph = [set() for _ in range(n+1)]
    visited = [False] * (n+1)
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i+1].add(j+1)
                graph[j+1].add(i+1)
    count = 0
    for i in range(1, n+1):
        if dfs(graph, i, visited):
            count += 1

    return count
