# dfs 로 특정 노드를 방문하고, 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        # dfs(x - 1, y)
        # dfs(x, y - 1)
        # dfs(x + 1, y)
        # dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = []
# row = []
for i in range(n):
    # row.append(input())
    graph.append(list(map(int, input())))
    # 한 줄의 00110 string 을 입력받은 후
    # string도 결국 배열이므로 map 함수를 통해
    # 각 원소에 int 메서드를 적용하여 list로 반환

# print(row) # ['00110', '00011', ...] 얘도 어차피 2차원 배열 아니노...
print(graph)  # [[0,0,1,1,0], ...]

result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 수행
        if dfs(i, j):
            result += 1

print(result)

# 씨이...발 뭐래눈고야...

