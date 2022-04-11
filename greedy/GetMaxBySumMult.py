# 곱하기 혹은 더하기로 최대값 구하기

n = input()

c = list(map(int, n))
result = c[0]

for i in range(1, len(n)):
    num = c[i]
    # 두 수 중 하나라도 0 혹은 1인 경우, 곱하기가 아닌 더하기 수행
    if num <= 1 or result <= 1:
        result = result + num
    else:
        result = result * num

print(result)

