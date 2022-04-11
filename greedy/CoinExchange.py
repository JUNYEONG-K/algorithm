# 동전 거스름돈 문제

n = int(input())
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count = count + n // coin
    n = n % coin

print(count)

