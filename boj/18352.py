# 다익스트라
import heapq
import sys
INF = int(1e9)


def main():
    n, m, k, x = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        # a번 노드에서 b번 노드로 가는 비용이 1
        graph[a].append([b, 1])
    # dp 테이블 개념, 출발노드로부터의 거리 저장
    distance = [INF] * (n+1)
    distance[0] = 0

    dijkstra(graph, x, distance)

    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
    if k not in distance:
        print(-1)


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


main()

