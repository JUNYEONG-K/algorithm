# 왜인지 모르겠지만 정렬되지 않음...ㅜㅜ
# def merge_sort(array):
#     if len(array) < 2:
#         return array
#     mid = len(array) // 2
#     low_arr = merge_sort(array[:mid])  # mid index 까지의 배열
#     high_arr = merge_sort(array[mid:])  # mid index 부터의 배열
#
#     merged_arr = []
#     low = 0
#     h = 0
#     while low < len(low_arr) and h < len(high_arr):
#         if low_arr[low] < high_arr[h]:
#             merged_arr.append(low_arr[low])
#             low += 1
#         else:
#             merged_arr.append(high_arr[h])
#             h += 1
#         merged_arr += low_arr[low:]
#         merged_arr += high_arr[h:]
#         return merged_arr

# 병합 결과를 담을 새로운 배열을 매번 생성해서 리턴하지 않고, 인덱스 접근을 이용해 입력 배열을 계속해서 업데이트 하면 메모리 사용량을 대폭 줄일 수 있다.
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))


array = [8, 4, 6, 2, 9, 1, 3, 7, 5]
merge_sort(array)
print(array)
