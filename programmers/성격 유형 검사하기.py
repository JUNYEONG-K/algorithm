from collections import defaultdict


def solution(survey, choices):
    answer = ''
    record = defaultdict(int)
    for i in range(len(survey)):
        if choices[i] == 1:
            record[survey[i][0]] += 3
        elif choices[i] == 2:
            record[survey[i][0]] += 2
        elif choices[i] == 3:
            record[survey[i][0]] += 1
        elif choices[i] == 4:
            continue
        elif choices[i] == 5:
            record[survey[i][1]] += 1
        elif choices[i] == 6:
            record[survey[i][1]] += 2
        elif choices[i] == 7:
            record[survey[i][1]] += 3
    print(record)
    if max(record['R'], record['T']) == record['R']:
        answer += 'R'
    else:
        answer += 'T'

    if max(record['C'], record['F']) == record['C']:
        answer += 'C'
    else:
        answer += 'F'

    if max(record['J'], record['M']) == record['J']:
        answer += 'J'
    else:
        answer += 'M'

    if max(record['A'], record['N']) == record['A']:
        answer += 'A'
    else:
        answer += 'N'
    print(answer)
    return answer
