def solution(s):
    answer = True

    array = []

    try:
        for i in s:
            if i == '(':
                array.append(1)
            else:
                array.pop()
    except:
        return False
    if len(array) == 0:
        return True
    return False
