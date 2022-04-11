# 모험가 길드 문제

N = int(input())
people = list(map(int, input().split()))
people.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in people:
    count += 1  # 현재 그룹에 해당 모험가 포함시키기
    if count >= i:
        result += 1  # 총 그룹의 수 증가
        count = 0  # 현재 그룹에 포함된 모험가 수 초기화

print(result)
