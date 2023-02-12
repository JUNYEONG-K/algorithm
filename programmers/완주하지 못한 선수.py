from collections import Counter


def solution(participant, completion):
    answer = 0
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


# Counter 객체 활용
def solution2(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]


def solution3(participant, completion):
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        print(dic)
        temp += int(hash(part))
        print(temp)
    for com in completion:
        temp -= hash(com)
        print(temp)
    answer = dic[temp]

    return answer


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
solution3(participant, completion)
