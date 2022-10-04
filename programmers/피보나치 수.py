def solution(n):
    answer = 0
    fibo = [0 for _ in range(n + 1)]
    fibo[1] = 1

    for i in range(2, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]

    return fibo[n] % 1234567


def solution2(n):
    answer = [0, 1]
    for i in range(2, n+1):
        answer.append(answer[i-1] + answer[i-2])
    return answer[-1]
