# 시각 문제 (00시 00분 00초 ~ N시 59분 59초까지 중 3이 하나라도 들어간 경우의 수)

hour = int(input())

# 가능한 모든 시각: 24 * 60 * 60 = 86,400 초
# 1초 => 2천만번 정도의 연산 수행 가정 (in python)

count = 0

for h in range(hour + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1

print(count)
