# binary search
def main():
    n, m = map(int, input().split())

    trees = list(map(int, input().split()))

    start = 1
    end = max(trees)

    print(binary_search(trees, m, start, end))


def binary_search(trees, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        mod = 0
        for tree in trees:
            if tree > mid:
                mod += tree - mid   # 자른 나머지
        if mod >= target:
            start = mid + 1
        elif mod < target:
            end = mid - 1
    return end  # 왜 mid 값이 아니고, end 값인 거지?


main()
