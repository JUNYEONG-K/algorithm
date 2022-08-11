# bfs
from collections import deque


def bfs(graph, start, visited):
    count = 0
    # 큐 구현을 위해 deque 라이브러리 사용
    # 큐에 시작 값 넣음
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        count += 1
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return count


def main():
    n = int(input())  # 컴퓨터 총 개수
    m = int(input())  # 간선 수

    # 2차원 배열 형성
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        # 양방향 연결
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n+1)
    print(bfs(graph, 1, visited) - 1)   # -1 하는 이유: 시작점 count 빼기


main()
