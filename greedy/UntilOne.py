# 1이 될 때까지 문제

n, k = map(int, input().split())
count = 0

while n != 1:
    if n % k != 0:
        n = n - 1
        count += 1
    else:
        n = n / k
        count += 1

print(count)

# 모범답안
# n, k = map(int, input().split())
# count = 0
#
# while True:
#     # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
#     target = (n // k) * k
#     count += (n - target)
#     n = target
#     # N이 K보다 작을 때(더 이상 나눌 수 없을 때 반복문 탈출)
#     if n < k:
#         break
#     # K로 나누기
#     count += 1
#     n = n // k
# # 마지막으로 남은 수에 대하여 1씩 빼기
# count += (n - 1)
# print(count)

