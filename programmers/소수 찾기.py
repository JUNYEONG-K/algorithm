from itertools import permutations


def checkPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    answer = []
    numbers = list(numbers)
    temp = []

    for i in range(1, len(numbers) + 1):
        print(list(permutations(numbers, i)))
        temp += list(permutations(numbers, i))
    print(temp)
    num = [int(''.join(t)) for t in temp]
    print(num)

    for i in num:
        if checkPrime(i):
            answer.append(i)

    return len(set(answer))
