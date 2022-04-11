# 1, 1, 2, 3, 5, 8, 13, 21, ...
# a(n) = a(n-1) + a(n-2)
# 배열이나 리스트를 사용


# 단순 재귀 함수 -> 피보나치 수열 계산 => 지수 시간 복잡도 가짐 O(2^N)
# fibo(6) 호출 시, f(2)가 여러 번 호출되는 것을 확인할 수 있다. (중복되는 문제)
def fibo_recursive(x):
    if x == 1 or x == 2:
        return 1
    return fibo_recursive(x - 1) + fibo_recursive(x - 2)


# 탑다운 다이나믹 프로그래밍
def fibo_top_down(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    d[x] = fibo_top_down(x-1) + fibo_top_down(x-2)
    return d[x]


def fibo_bottom_up(x, n):
    for i in range(3, n+1):
        x[i] = x[i-1] + x[i-2]
    return x[i]


# 1. 최적 부분 구조: 큰 문제를 작은 문제로 나눌 수 있다. (fibo(6) -> fibo(5) + fibo(4))
# 2. 중복되는 부분 문제: 동일한 작은 문제를 반복적으로 해결한다. (특정 x에 대해 fibo(x) 여러번 호출됨)
print(fibo_recursive(4))


# 한 번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d = [0] * 100
print(fibo_top_down(99))    # O(N)


# 한 번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d = [0] * 100
d[1] = 1
d[2] = 1
print(fibo_bottom_up(d, 99))

