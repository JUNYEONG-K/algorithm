def solution(answers):
    first = [1, 2, 3, 4, 5] * (10000 // 5)
    second = [2, 1, 2, 3, 2, 4, 2, 5] * (10000 // 8)
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (10000 // 10)
    answer = answers * (10000 // 5)
    candidates = [0] * 4
    for p, q, r, a in zip(first, second, third, answers):
        if p == a:
            candidates[1] += 1
        if q == a:
            candidates[2] += 1
        if r == a:
            candidates[3] += 1

    result = []
    for i in range(1, 4):
        if candidates[i] == max(candidates):
            result.append(i)

    return result
