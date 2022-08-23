def solution(triangle):
    # dp 테이블 초기화 -> dp 테이블 초기화에 너무 쓸데없는 코드들을 낭비했다.
    dp = []
    length = []
    for i in range(len(triangle)):
        length.append(len(triangle[i]))
    for i in length:
        line = []
        for j in range(i):
            line.append(0)
        dp.append(line)
    # 점화식
    dp[0][0] = triangle[0][0]
    # dp[1][0] = dp[0][0] + triangle[1][0]
    # dp[1][1] = dp[0][0] + triangle[1][1]
    # dp[2][0] = dp[1][0] + triangle[2][0]
    # dp[2][1] = max(dp[1][0] + triangle[2][1], dp[1][1] + triangle[2][1])
    # dp[2][2] = dp[1][2] + triangle[2][2]
    # dp[3][0] = dp[2][0] + triangle[3][0]
    # dp[3][1] = max(dp[2][0] + triangle[3][1], dp[2][1] + triangle[3][1])
    # dp[3][2] = max(dp[2][1] + triangle[3][2], dp[2][2] + triangle[3][2])
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i - 1][0] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1] + triangle[i][j], dp[i - 1][j] + triangle[i][j])
    # 2차원 배열 최대값 찾기 -> map 함수 유용!
    max_value = max(map(max, dp))
    return max_value
