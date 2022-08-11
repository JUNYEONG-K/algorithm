n, m, k = map(int, input().split())  # n, m, k 값 입력 받기
data = list(map(int, input().split()))  # 한줄에 입력된 값들 배열로 받기

data.sort()  # 오름차순 정렬
first = data[n-1]   # 가장 큰 수
second = data[n-2]  # 두 번째로 큰 수

result = 0  # 결과값

while True:
    for i in range(k):  # 가장 큰 수 k번 더하기
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:  # 두 번째로 큰 수, 중간 중간에 한 번씩 더해주기
        break
    result += second
    m -= 1

print(result)
