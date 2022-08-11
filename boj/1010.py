# dp 로 분류되어있지만 조합으로 풀리기 때문에 조합으로 풀어봄
import math

case = int(input())

for _ in range(case):
    n, m = map(int, input().split())

    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)
