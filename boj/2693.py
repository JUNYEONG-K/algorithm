n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    graph[i].sort()
    print(graph[i][7])

