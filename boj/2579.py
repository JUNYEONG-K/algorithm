n = int(input())

steps = []
for _ in range(n):
    steps.append(int(input()))
# 해당 계단을 무조건 밟는 경우의 값 기록
dp = [0] * (n+1)
# 첫번째 계단 밟는 경우
dp[0] = steps[0]
# 두번째 계단 밟는 경우
dp[1] = steps[0] + steps[1]
# 세번째 계단 밟는 경우
dp[2] = max(steps[0] + steps[2], steps[1] + steps[2])

for i in range(3, n):
    dp[i] = max(dp[i-3] + steps[i-1] + steps[i], dp[i-2] + steps[i])

print(dp[n-1])
