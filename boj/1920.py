# binary search
def main():
    n = int(input())
    num = list(map(int, input().split()))
    num.sort()

    m = int(input())
    target = list(map(int, input().split()))
    result = [0] * m

    for i in range(m):
        if binary_search(num, target[i], 0, n - 1):
            result[i] = 1
        print(result[i])


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


main()
