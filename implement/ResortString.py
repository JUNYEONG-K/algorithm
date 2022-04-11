# 문자열 재정렬

data = input()
result = []
value = 0

for s in data:
    # 알파벳 여부 확인
    # if ord('A') <= int(s) <= ord('Z'):
    if s.isalpha():
        result.append(s)
    else:
        value += int(s)

result.sort()

# list 를 문자열로 반환하는 방법 중 하나 => 띄어쓰기 불가
# str1 = ""
# for i in result:
#   str1 += i

# print(str1+str(value))

# 모범 답안
result.append(str(value))
# list 를 문자열로 반환하는 방법 중 하나 => 띄어쓰기 가능
print(''.join(result))

