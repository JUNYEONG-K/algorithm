# 왕실의 나이트 문제

init = input()
# ord func => 아스키코드 값 반환
x = int(ord(init[0]))
y = int(init[1])

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0

for step in steps:
    next_row = x + step[0]
    next_column = y + step[1]
    if int(ord('a')) <= next_row <= int(ord('h')) and 1 <= next_column <= 8:
        result += 1

print(result)

