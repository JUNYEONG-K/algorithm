from collections import deque


def solution(n, words):
    answer = []
    answer.append(words[0])
    result = deque(words[1:])
    count = 0
    for _ in range(len(words)-1):
        count += 1
        word = result.popleft()
        compare2 = list(word)
        compare = list(answer[-1])
        if compare[-1] == compare2[0] and answer.count(word) == 0:
            answer.append(word)
        else:
            a = count % n + 1
            b = count // n + 1
            return [a, b]
    return [0, 0]
