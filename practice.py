import uuid
from collections import deque


def _1026():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)
    s = 0
    for i in range(n):
        s += a[i] * b[i]
    print(s)


def _1065():
    n = int(input())
    hansu = 0

    for i in range(1, n + 1):
        if i <= 99:
            hansu += 1
        else:
            num = list(map(int, str(i)))
            if num[0] - num[1] == num[1] - num[2]:
                hansu += 1
    print(hansu)

    print()


def _1764():
    n, m = map(int, input().split())
    no_hear = set()
    no_seen = set()

    for _ in range(n):
        no_hear.add(input())
    for _ in range(m):
        no_seen.add(input())

    result = sorted(list(no_seen & no_hear))
    print(len(result))
    for i in result:
        print(i)


def _1920():
    n = int(input())
    candidate = list(map(int, input().split()))
    candidate.sort()  # for binary search
    m = int(input())
    target = list(map(int, input().split()))
    result = [0] * m
    for num in target:
        print(binary_search_1920(candidate, num, 0, n - 1))


# 한번더
def binary_search_1920(candidate, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if candidate[mid] == target:
            return 1
        elif target < candidate[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 0


# 한번더
def _11047():
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))
    coins.sort(reverse=True)
    count = 0
    while k > 0:
        # for coin in coins:
        #     if coin <= k:
        #         count += k // coin
        #         k = k % coin
        for coin in coins:
            count += k // coin  # coin이 k보다 크면 어차피 0임
            k = k % coin
    print(count)


# 한번더
def _11399():
    n = int(input())
    times = list(map(int, input().split()))
    times.sort()
    total = 0
    # 누적합 계산
    for i in range(n):
        for j in range(i + 1):
            total += times[j]
    print(total)


# 한번더
def _16173():
    n = int(input())
    graph = []
    visited = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
        visited.append([False] * n)
    if dfs16173(0, 0, graph, visited, n):
        print("Hing")


def dfs16173(x, y, graph, visited, n):
    dx = [1, 0]
    dy = [0, 1]

    if x >= n or x <= -1 or y >= n or y <= -1:
        return 0
    elif visited[x][y]:
        return 0
    elif graph[x][y] == -1:
        print("HaruHaru")
        exit()
    else:
        visited[x][y] = True
        for i in range(2):
            nx = x + dx[i] * graph[x][y]
            ny = y + dy[i] * graph[x][y]
            dfs16173(nx, ny, graph, visited, n)
        return True


# 한번더
def _1431():
    n = int(input())
    guitars = []
    for _ in range(n):
        guitars.append(input())
    for i in range(n - 1):
        for j in range(i + 1, n):
            if len(guitars[i]) > len(guitars[j]):
                guitars[i], guitars[j] = guitars[j], guitars[i]
            elif len(guitars[i]) == len(guitars[j]):
                suma = 0
                sumb = 0
                for x, y in zip(guitars[i], guitars[j]):
                    if x.isdigit():
                        suma += int(x)
                    if y.isdigit():
                        sumb += int(y)
                if suma > sumb:
                    guitars[i], guitars[j] = guitars[j], guitars[i]
                elif suma == sumb:
                    for x, y in zip(guitars[i], guitars[j]):
                        if x > y:
                            guitars[i], guitars[j] = guitars[j], guitars[i]
                            break
                        elif x < y:
                            break
    for guitar in guitars:
        print(guitar)


# 한번더
def _1463():
    n = int(input())
    count = 0
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
    print(dp[n])


def _2579():
    n = int(input())
    stairs = [0] * (n + 1)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        stairs[i] = int(input())
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])
    print(dp[n])


def dfs2606(param):
    pass


def _2606():
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n + 1)
    print(bfs2606(graph, visited, 1) - 1)


def bfs2606(graph, visited, node):
    count = 0
    q = deque([node])
    visited[node] = True
    while q:
        v = q.popleft()
        count += 1
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return count


# 골 때리는 문제... 한번더
def _1012():
    t = int(input())
    test = [0 for _ in range(t)]
    for x in range(t):
        n, m, count = map(int, input().split())

        # 배추밭 그림
        graph = [[0] * m for _ in range(n)]
        for _ in range(count):
            a, b = map(int, input().split())
            graph[a][b] = 1
        print(graph)
        for i in range(n):
            for j in range(m):
                # 현재 위치에서 dfs 수행
                if dfs1012(graph, i, j, n, m):
                    test[x] += 1

    for i in range(t):
        print(test[i], end='\n')


def dfs1012(graph, x, y, w, l):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= w or ny < 0 or ny >= l:
            return False
        if graph[nx][ny] == 1:
            dfs1012(graph, nx, ny, w, l)
            return True
        return False


def _1260():
    n, m, start_node = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)

    # 시작 노드를 스택에 쌓고 (== 함수 콜 하고)
    dfs1260(graph, 1, visited)
    visited = [False] * (n + 1)
    print()
    bfs1260(graph, 1, visited)


def dfs1260(graph, node, visited):
    # 방문 처리
    visited[node] = True
    print(node, end=' ')
    for i in graph[node]:
        if not visited[i]:
            dfs1260(graph, i, visited)


def bfs1260(graph, start_node, visited):
    # 시작 노드를 큐에 삽입 하고, 방문 처리
    q = deque([start_node])
    visited[start_node] = True
    while q:
        # 큐에서 하나 꺼내서
        v = q.popleft()
        print(v, end=' ')
        # 인접 노드 조사
        for i in graph[v]:
            if not visited[i]:
                # 큐에 삽입 하고, 방문 처리
                q.append(i)
                visited[i] = True


# 한번더
def _2644():
    people = int(input())
    x, y = map(int, input().split())
    n = int(input())

    graph = [[] for _ in range(people + 1)]
    for _ in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    relation = [0] * (people + 1)
    # bfs2644(graph, x, relation)
    dfs2644(graph, x, relation)
    print(relation[y] if relation[y] > 0 else -1)


def bfs2644(graph, start, relation):
    q = deque([start])
    while q:
        v = q.popleft()
        for i in graph[v]:
            if relation[i] == 0:
                q.append(i)
                relation[i] = relation[v] + 1


def dfs2644(graph, start, relation):
    # 방문처리할 거 없음
    # 스택에 넣고 방문처리하던 것과 달리, 방문처리 하고 스택에 넣는 방식
    for i in graph[start]:
        if relation[i] == 0:
            relation[i] = relation[start] + 1
            dfs2644(graph, i, relation)


# 왜 end값을 출력할까...
def _2805():
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))
    start, end = 0, max(trees)

    while start <= end:
        mid = (start + end) // 2
        result = 0
        for tree in trees:
            mod = tree - mid
            if mod < 0:
                mod = 0
            result += mod

        if result >= m:
            start = mid + 1
        elif result < m:
            end = mid - 1
    print(end)


# 한번더,,, 왜 x, y 값 위치가 바뀌었을까...
def _4963():
    while True:
        w, h = map(int, input().split())
        if w == 0 & h == 0:
            break
        graph = []
        for _ in range(h):
            graph.append(list(map(int, input().split())))
        island = 0
        for i in range(h):
            for j in range(w):
                if dfs4963(graph, i, j, w, h):
                    island += 1
        print(island)


def dfs4963(graph, y, x, w, h):
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]
    if x < 0 or x >= w or y < 0 or y >= h:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs4963(graph, y, x - 1, w, h)
        dfs4963(graph, y, x + 1, w, h)
        dfs4963(graph, y - 1, x, w, h)
        dfs4963(graph, y + 1, x, w, h)
        dfs4963(graph, y - 1, x - 1, w, h)
        dfs4963(graph, y - 1, x + 1, w, h)
        dfs4963(graph, y + 1, x - 1, w, h)
        dfs4963(graph, y + 1, x + 1, w, h)
        return True
    return False


# 한번더? 아이디어 생각해내기가 어려움
def _11053():
    n = int(input())
    arrays = list(map(int, input().split()))
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if arrays[j] < arrays[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))


def _11724():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    count = 0
    for i in range(1, n+1):
        if not visited[i]:
            bfs11724(graph, i, visited)
            count += 1
    print(count)


def dfs11724(graph, node, visited):
    # 방문처리
    visited[node] = True
    # 스택에 넣기 (인접 노드 중 방문안한거)
    for i in graph[node]:
        if not visited[i]:
            dfs11724(graph, i, visited)


def bfs11724(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


def _11725():
    n = int(input())
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    parent = [0] * (n+1)
    dfs11725(tree, 1, parent)
    for i in range(2, n+1):
        print(parent[i], end='/n')


def dfs11725(tree, node, parent):
    # 방문처리 -> ?
    # 인접 노드 검사
    for i in tree[node]:
        if parent[i] == 0:  # 부모가 안정해졌다면
            parent[i] = node
            dfs11725(tree, i, parent)


def _16401():
    m, n = map(int, input().split())
    targets = list(map(int, input().split()))
    start, end = 0, max(targets)

    while start <= end:
        mid = (start + end) // 2
        count = 0
        for target in targets:
            count += target // mid
        if count == m:
            print(mid)
            return
        elif count > m:
            start = mid + 1
        else:
            end = mid - 1
    print(0)


def _2178():
    n, m = map(int, input().split())
    maze = []
    for _ in range(n):
        maze.append(list(map(int, input())))
    bfs2178(maze, 0, 0, n, m)
    print(maze[n-1][m-1])


def bfs2178(graph, start_x, start_y, n, m):
    q = deque()
    q.append((start_x, start_y))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


_2178()
# _16401()
# _11725()
# _11724()
# _11053()
# _4963()
# _2805()
# _2644()
# _1260()
# _1012()
# _2606()
# _2579()
# _1463()
# _1431()
# _16173()
# _11399()
# _11047()
# _1920()
# _1764()
# _1065()
# _1026()
