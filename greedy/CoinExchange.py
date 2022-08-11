# 동전 거스름돈 문제

n = int(input())
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count = count + n // coin   # 동전 개수 카운트
    n = n % coin    # 거슬러 주고 남은 돈

print(count)

