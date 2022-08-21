# stack/queue
def solution(array, commands):
    answer = []
    for p in range(len(commands)):
        i, j, k = commands[p][0], commands[p][1], commands[p][2] - 1
        # 배열 슬라이싱
        test = array[i-1:j]
        test.sort()
        answer.append(test[k])
    return answer
