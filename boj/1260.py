# bfs, dfs
from collections import deque


# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    # 큐에 시작 값 넣음
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def main():
    n, m, v = map(int, input().split())
    visited = [False] * (n+1)
    test = [
        [],
        [2, 3, 4],  # 1번 노드의 인접 노드
        [1, 4],     # 2벙 노드의 인접 노드
        [1, 4],     # 3번 노드의 인접 노드
        [1, 2, 3]   # 4번 노드의 인접 노드
    ]
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        # 아래 두 줄이 핵심!!
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, n+1):
        # 인접 노드 중 작은 번호부터 방문하기 위해서
        graph[i].sort()
    dfs(graph, v, visited)
    print()
    visited = [False] * (n+1)
    bfs(graph, v, visited)


main()
