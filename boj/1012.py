# dfs, CountIce 와 비슷한 문제
# bfs 로 풀면 Runtime Error (Recursive Error) 가 발생하지 않는다고 한다.
# 파이썬에서는 1,000번 이상의 recursion 이 발생하면 recursion error 가 발생한다고 한다.
# 백준에 처음 풀이해서 제출한 답에 import 문 적은 것이 맞았다 ㅅㅂ
import sys
sys.setrecursionlimit(100000)


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        graph[x][y] = 0
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


t = int(input())
test = [0 for _ in range(t)]
for x in range(t):
    n, m, count = map(int, input().split())

    # 배추밭 그림
    graph = [[0] * m for _ in range(n)]
    for _ in range(count):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for i in range(n):
        for j in range(m):
            # 현재 위치에서 dfs 수행
            if dfs(i, j):
                test[x] += 1

for i in range(t):
    print(test[i], end='\n')
