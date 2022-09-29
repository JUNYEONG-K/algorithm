def solution(babbling):
    can_speak = ["aya", "ye", "woo", "ma"]

    for i in range(len(babbling)):
        for j in range(4):
            if can_speak[j] + can_speak[j] in babbling[i]:
                continue
            if can_speak[j] in babbling[i]:
                babbling[i] = babbling[i].replace(can_speak[j], "")

    return babbling.count('')
