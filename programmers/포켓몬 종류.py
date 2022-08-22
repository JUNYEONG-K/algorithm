def solution(nums):
    # 중복 제거 -> 동물의 종류 수 구하기
    # result = set(nums)
    # if len(result) > len(nums) // 2:
        # return len(nums) // 2
    # return len(result)
    return min(len(nums) // 2, len(set(nums)))
