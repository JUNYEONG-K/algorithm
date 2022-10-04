def my_solution(numbers, hand):
    answer = ''
    left = {1, 4, 7}
    right = {3, 6, 9}
    present_left, present_right = 0, 0
    for i in numbers:
        print(present_left, present_right, answer)
        if i in left:
            answer += 'L'
            present_left = i
        elif i in right:
            answer += 'R'
            present_right = i
        else:
            if i - present_left < i - present_right - 2:
                answer += 'L'
                present_left = i
            elif i - present_right - 2 < i - present_left:
                answer += 'R'
                present_right = i
            else:
                if hand == "left":
                    answer += 'L'
                    present_left = i
                else:
                    answer += 'R'
                    present_right = i

    print(answer)
    return answer


def findDistance(currentN, nextN):
    keypad = {1: [0, 0], 2: [1, 0], 3: [2, 0],
              4: [0, 1], 5: [1, 1], 6: [2, 1],
              7: [0, 2], 8: [1, 2], 9: [2, 2],
              "*": [0, 3], 0: [1, 3], "#": [2, 3]}
    x1, y1 = keypad[currentN]
    x2, y2 = keypad[nextN]
    return abs(x1 - x2) + abs(y1 - y2)


def solution(numbers, hand):
    answer = ''
    current_l, current_r = '*', '#'

    for i in numbers:
        if i in (1, 4, 7):
            answer += 'L'
            current_l = i
        elif i in (3, 6, 9):
            answer += 'R'
            current_r = i
        else:
            if findDistance(current_l, i) < findDistance(current_r, i):
                answer += 'L'
                current_l = i
            elif findDistance(current_r, i) < findDistance(current_l, i):
                answer += 'R'
                current_r = i
            else:
                if hand == 'left':
                    answer += 'L'
                    current_l = i
                else:
                    answer += 'R'
                    current_r = i

    return answer
