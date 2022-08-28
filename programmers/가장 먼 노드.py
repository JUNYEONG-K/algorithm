import heapq

INF = int(1e9)


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for i in range(len(edge)):
        a, b = edge[i][0], edge[i][1]
        graph[a].append([b, 1])
        graph[b].append([a, 1])
    distance = [INF] * (n + 1)
    distance[0] = 0

    dijkstra(graph, 1, distance)

    print(distance)
    return distance.count(max(distance))


def dijkstra(graph, start_node, distance):
    q = []
    distance[start_node] = 0
    heapq.heappush(q, (distance[start_node], start_node))

    while q:
        dist, now = heapq.heappop(q)

        for next_node, next_cost in graph[now]:
            cost = dist + next_cost

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))