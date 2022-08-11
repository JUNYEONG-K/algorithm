# bfs (dfs 가 아닌 이유: dfs 는 모든 노드를 거치기 때문에 오래 걸려 런타임 에러가 뜬다. 최단거리일 때는 bfs)
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
# graph = [list(map(int, input())) for _ in range(n)]


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0 , -1, 1]

    q = deque()
    q.append((x, y))    # 현재 위치 추가

    while q:
        x, y = q.popleft()  # 현재 위치의 인접노드를 탐색하기 위해
        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 벗어낰 -> 아무 작업 x
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽 -> 아무 작업 x
            if graph[nx][ny] == 0:
                continue
            # 갈 수 있는 길
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[n-1][m-1]


print(bfs(0, 0))
