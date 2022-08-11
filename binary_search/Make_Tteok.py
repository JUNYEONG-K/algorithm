# 절단기의 높이는 0 ~ 10억까지의 정수 중 하나 => 큰 탐색 범위를 보면 이진탐색을 떠올린다!
# 적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 H를 반복해서 조정하면 된다.
# 높이가 올라가면 얻을 수 있는 떡길이가 줄고, 높이가 낮아지면 얻을 수 잇는 떡길이가 늘기 때문!!

# 떡의 개수, 요청한 떡 길이
n, k = map(int, input().split())
# 떡의 길이들
tteok = list(map(int, input().split()))

start, end = 0, max(tteok)
result = 0

while start <= end:
    total = 0
    mid = (start+end) // 2
    for x in tteok:
        if x > mid:  # 잘랐을 때 떡의 양 계산
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기
    if total < mid:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기
    else:
        result = mid
        start = mid + 1

print(result)