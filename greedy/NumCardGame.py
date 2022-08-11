n, m = map(int, input().split())

result = 0  # 비교군

for i in range(n):
    data = list(map(int, input().split()))  # 한 줄씩 입력 받기
    min_value = min(data)   # 해당 줄에서 가장 작은 값
    result = max(result, min_value)  # 작은 값들 중 가장 큰 값을 찾기

print(result)
