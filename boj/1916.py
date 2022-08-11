# 다익스트라
import heapq
import sys
INF = int(1e9)


def dijkstra(graph, start_node, distance):
    q = []
    distance[start_node] = 0
    heapq.heappush(q, (distance[start_node], start_node))

    while q:
        dist, now = heapq.heappop(q)

        # 꼭 필요한 코드인가? 흐음...
        if distance[now] < dist:
            continue

        for next_node, next_cost in graph[now]:
            cost = dist + next_cost

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))


def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append([b, c])

    start, end = map(int, sys.stdin.readline().split())
    distance = [INF] * (n+1)
    dijkstra(graph, start, distance)

    print(distance[end])


main()
