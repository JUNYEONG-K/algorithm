def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]      # 미리 puddles 좌표 거꾸로
    dp = [[0] * (m + 1) for i in range(n + 1)]  # dp 초기화
    dp[1][1] = 1           # 집의 위치(시작위치)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue
            if [i, j] in puddles:    # 웅덩이 위치의 경우 값을 0으로
                dp[i][j] = 0
            else:                    # 현재 칸은 왼쪽 칸, 위 칸의 합산!
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp[n][m]
# dp 테이블을 1번부터 사용하는 이유
# dp 테이블을 0번부터 사용할 경우 i-1이나 j-1과 같은 상황에서 -1값이 나와, 테이블의 맨 끝값이 덧셈에 영향을 준다.
# dp 테이블을 1번부터 사용하면 i-1이나 j-1이 0인 상황, 즉 범위를 벗어나는 테두리의 상황에서도 더해지는 값이 0이 되어 결과에 영향을 미치지 않는다.
