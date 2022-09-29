def solution(num, total):
    answer = []
    x = total // num
    answer.append(x)
    if num % 2 == 0:
        for i in range(1, num // 2):
            answer.append(x - i)
        for i in range(1, num // 2 + 1):
            answer.append(x + i)
    else:
        for i in range(1, num // 2 + 1):
            answer.append(x - i)
            answer.append(x + i)
    answer.sort()
    return answer

#     result = [i+1 for i in range(1001)]
#     test = []
#     if total == 0:
#         for i in range(num):
#             test.append(i - num//2)
#         return test
#     for i in range(total):
#         if sum(result[0+i:i+num]) == total:
#             return result[0+i:i+num]
