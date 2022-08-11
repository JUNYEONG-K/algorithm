# dfs
# def dfs(x, y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         dfs(x - 1, y)
#         dfs(x + 1, y)
#         dfs(x, y - 1)
#         dfs(x, y + 1)
#         dfs(x - 1, y - 1)
#         dfs(x - 1, y + 1)
#         dfs(x + 1, y - 1)
#         dfs(x + 1, y + 1)
#         return True
#     return False
#
#
# while True:
#     n, m = map(int, input().split())
#
#     if n == 0 & m == 0:
#         break
#
#     graph = []
#     for _ in range(m):
#         graph.append(list(map(int, input().split())))
#
#     result = 0
#     for i in range(n):
#         for j in range(m):
#             if dfs(i, j):
#                 result += 1
#
#     print(result)
def dfs(y, x):
    if x < 0 or x >= w or y < 0 or y >= h:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(y, x - 1)
        dfs(y, x + 1)
        dfs(y - 1, x)
        dfs(y + 1, x)
        dfs(y - 1, x - 1)
        dfs(y - 1, x + 1)
        dfs(y + 1, x - 1)
        dfs(y + 1, x + 1)
        return True
    return False


while True:
    w, h = map(int, input().split())

    if w == 0 & h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                result += 1
    print(result)
