# 다익스트라
import heapq
INF = int(1e9)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dijkstra():
    # heap queue 준비
    q = []
    # 출발노드에서 소비되는 비용(기준값)과 출발노드 설정
    heapq.heappush(q, (graph[0][0], 0, 0))
    # 출발노드에서의 거리는 0
    distance[0][0] = 0

    # q 가 비어있지 않은 동안
    while q:
        # 기준값과 위치값(x, y)
        cost, x, y = heapq.heappop(q)

        if x == n-1 and y == n-1:
            print(f'Problem {count}: {distance[x][y]}')
            break

        # 상하좌우로 이동하며 ...
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # 이동 위치가 범위 내에 있을 때 ...
            if 0 <= new_x < n and 0 <= new_y < n:
                # 이동 위치를 거쳐갈 때의 소비 비용
                new_cost = cost + graph[new_x][new_y]
                # 이동 위치를 거쳐갈 때의 소비 비용이 바로 가서 잃는 것보다 적을 때
                if new_cost < distance[new_x][new_y]:
                    distance[new_x][new_y] = new_cost
                    heapq.heappush(q, (new_cost, new_x, new_y))


count = 1


while True:
    n = int(input())
    if n == 0:
        break

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    # ??
    distance = [[INF] * n for _ in range(n)]

    dijkstra()
    count += 1


