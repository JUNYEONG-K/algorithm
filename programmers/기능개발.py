def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        mod = 100 - progresses[i]
        if (mod % speeds[i]) > 0:
            day = mod // speeds[i] + 1
        else:
            day = mod // speeds[i]
        days.append(day)
    print(days)
    answer = []

    index = 0
    for i in range(len(days)):
        if days[index] < days[i]:
            answer.append(i - index)
            index = i
    answer.append(len(days) - index)
    return answer
