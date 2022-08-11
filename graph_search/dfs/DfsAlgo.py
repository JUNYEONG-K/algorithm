def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# main 없이 하면 오류는 아니고 경고가 뜨는데, 전역변수 사용이 문제가 되어서 그런 것 같다.
# 이건 나중에 한번 공부해보자
# Shadows name 으로 구글링했을 때 나온 해결!
def main():
    # 각 노드가 연결된 정보를 표현 (2차원 리스트)
    # 각 노드의 인접 노드 값
    graph = [
        [],
        [2, 3, 8],  # 1번 노드와 인접한 노드
        [1, 7],     # 2번 노드와 인접한 노드
        [1, 4, 5],  # 3번 노드와 인접한 노드
        [3, 5],     # 4번 노드와 인접한 노드
        [3, 4],     # 5번 노드와 인접한 노드
        [7],        # 6번 노드와 인접한 노드
        [2, 6, 8],  # 7번 노드와 인접한 노드
        [1, 7]      # 8번 노드와 인접한 노드
    ]

    # 각 노드가 방문된 정보를 표현 (1차원 리스트)
    visited = [False] * 9

    # 정의된 DFS 함수 호출
    dfs(graph, 1, visited)


main()

# for i in graph[1]:
# 	i = 2, 3, 8
# 	i = 2 -> 2번 노드 방문했니? 아니 -> dfs(2)
# 		for i in graph[2]:
# 			i = 1, 7
# 			i = 1 -> 1번 방문했니? yes, 7번 방문했니? 아니 -> dfs(7)
# 				for i in graph[7]:
# 					i = 2, 6, 8
# 					i = 2 방문, 6 방문했니? 아니 -> dfs(6)
# 						for i in graph[6]:
# 							i = 7
# 							i = 7 방문했음,
# 					i = 8 방문햇니? 아니 -> dfs(8)
# 						for i in graph[8]:
# 							i = 1, 7 이미 모두 방문했음, 끝!
# 	i = 3 -> 3번 노드 방문했니? 아니 -> dfs(3)
# 		for i in graph[3]:
# 			i = 1, 4, 5
# 			i = 1 이미 방문, 4방문했니? 아니 -> dfs(4)
# 				for i in graph[4]:
# 					i = 3, 5
# 					i = 3 방문, 5방문? 아니 -> dfs(5)
# 						for i in graph[5]:
# 							i = 3, 4
# 							i = 3방문, 4 방문 끝!
# 			i = 5 방문했니? 응, 끝
# 	i = 8 -> 8도 이미 방문했으니 끝
# 끝!
