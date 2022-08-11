# 상하좌우 이동

n = int(input())
plans = list(input().split())   # list 안 붙여도 됨
x, y = 1, 1

# 동, 서, 남, 북
dx = [0, 0, 1, -1]  # (가로축)
dy = [1, -1, 0, 0]  # (세로축)
move_types = ['R', 'L', 'D', 'U']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)

