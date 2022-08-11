# gcd 최대공약수
import math


# 재귀
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# 위의 방식으로는 메모리 초과가 날 수 있음
def gcdV2(a, b):
    while b:
        a, b = b, a % b
    return a


n, m = map(int, input().split())
# 아래의 방식으로는 시간초과 판정을 받았다!
# a = b = '1'
# for _ in range(n-1):
#     a += '1'
# for _ in range(m-1):
#     b += '1'
#
# print(math.gcd(int(a), int(b)))
print('1' * math.gcd(n, m))
