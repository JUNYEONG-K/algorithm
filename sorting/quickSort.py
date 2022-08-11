def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # pivot 은 첫번째 원소
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:  # pivot 보다 큰 데이터를 찾을 때까지 반복
            left += 1
        while right > start and array[right] > array[pivot]:  # pivot 보다 작은 데이터를 찾을 때까지 반복
            right -= 1
        if left > right:  # 엇갈렸다면 작은 데이터와 pivot 을 교체함으로서 왼쪽파트엔 pivot 보다 작은 값들, 오른쪽 파트에는 pivot 보다 큰 값들!!
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 두 수 교체 => 작은거 왼쪽 파트, 큰 거 오른쪽 파트
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


# 파이썬의 장점을 살린 퀵 정렬
def quick_sort(array):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    # arr[A:B:C] 의미 -> index A부터 index B까지 C의 간격으로 배열을 만든다
    # 따라서 tail 은 5 ~ 8 인 배열에서 7 ~ 8 인 배열을 만들어낸 것!
    # 즉 tail 은 pivot 을 제외한 배열
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


def main():
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    print(quick_sort(array))
    # quick_sort(array, 0, len(array) - 1)
    print(array)


main()
