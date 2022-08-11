# 다익스트라
import heapq
INF = int(1e9)

n, m, x = map(int, input().split())

# 2 차원 배열
graph = [[] for i in range(n + 1)]

for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def dijkstra(start_node):
    q = []
    # start_node 에서 각 node로 이동하는 거리 (배열)
    distance = [INF] * (n + 1)

    heapq.heappush(q, (0, start_node))
    distance[start_node] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 이미 최단 거리임이 확정된 경우
        if distance[now] < dist:
            continue

        # 인접한 노드 확인 (다음 노드와 다음 노드까지의 비용)
        for node_index, node_cost in graph[now]:
            # 다음 노드를 거쳐갈 때의 총 비용
            cost = dist + node_cost
            # 다음 노드를 거쳐갈 때의 총 비용이 바로 가는 것보다 적을 때
            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance


result = 0

for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)
