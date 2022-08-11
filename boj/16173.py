# dfs
def main():
    n = int(input())

    graph = []
    visited = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
        visited.append([False] * n)

    if dfs(0, 0, graph, visited, n):
        print("Hing")


def dfs(x, y, graph, visited, n):
    # 오른쪽, 아래쪽 이동방향
    dx = [0, 1]
    dy = [1, 0]

    if x >= n or x <= -1 or y >= n or y <= -1:
        return 0
    elif visited[x][y]:
        return 0
    elif graph[x][y] == -1:
        print("HaruHaru")
        exit()
    else:
        visited[x][y] = True    # 방문처리 (이외 추가 작업 할 수 있음)
        for i in range(2):      # dfs 할 곳으로 이동
            nx = x + dx[i] * graph[x][y]
            ny = y + dy[i] * graph[x][y]
            dfs(nx, ny, graph, visited, n)
        return True


main()
