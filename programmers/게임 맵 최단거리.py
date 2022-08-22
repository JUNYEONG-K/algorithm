from collections import deque


def solution(maps):
    # 동서남북 이동방향
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 맵 가로, 세로 크기
    n, m = len(maps), len(maps[0])
    # maps와 같은 크기의 2차원 배열 -> 이동 칸 수 계산
    visited = [[0 for _ in range(m)] for _ in range(n)]

    def bfs(i, j):
        # 출발 노드를 거쳐야함으로 1
        visited[0][0] = 1
        # 출발 노드 삽입
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            # 목적지 도착하면 중단
            if x == n - 1 and y == m - 1:
                return visited[x][y]
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                # maps 범위 내에 존재하는지 & 아직 방문하지 않은 곳인지 & 이동할 수 있는 곳인지 확인
                if 0 <= next_x <= n - 1 and 0 <= next_y <= m - 1 and visited[next_x][next_y] == 0 and maps[next_x][
                    next_y] == 1:
                    visited[next_x][next_y] = visited[x][y] + 1
                    q.append((next_x, next_y))
        # 끝끝내 도달하지 못했으면 -1 return
        return -1

    return bfs(0, 0)