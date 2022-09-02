def solution(new_id):
    rule = ['.', '-', '_']
    # 1, 2단계
    for i in new_id:
        if i.isupper():
            new_id = new_id.replace(i, i.lower())
        elif i.islower():
            continue
        elif i.isdigit():
            continue
        elif i not in rule:
            new_id = new_id.replace(i, "")
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace("..", ".")
    # 4단계
    new_id = new_id.strip(".")
    # 5단계
    if new_id == "":
        new_id += 'a'
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id.rstrip(".")
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    answer = new_id
    print(answer)
    return answer
