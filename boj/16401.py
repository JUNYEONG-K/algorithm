# binary search
n, m = map(int, input().split())
snacks = list(map(int, input().split()))

start = 0
end = max(snacks)

# 과자 길이
result = 0
while start <= end:
    # 나누어줄 수 있는 과자 개수
    count = 0

    mid = (start + end) // 2

    if mid == 0:
        count = 0
        break

    for snack in snacks:
        if snack - mid >= 0:
            count = count + (snack // mid)

    if count == n:
        result = mid
        break
    elif count > n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
