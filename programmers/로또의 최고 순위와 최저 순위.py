def solution(lottos, win_nums):
    answer = []
    # 당첨된 번호 개수
    count = 0
    # 0으로 표시된 번호 개수
    zero = 0
    for lotto in lottos:
        if lotto == 0:
            zero += 1
        if lotto in win_nums:
            count += 1
    print(count, count + zero)

    # 0으로 적힌 번호가 당첨이라고 가정한 경우의 순위
    answer.append(7 - (count + zero))
    # 0으로 적힌 번호가 당첨이 아니라고 가정한 경우의 순위
    answer.append(7 - count)

    # 그 외 처리 (0개 맞았을 때)
    if answer[0] >= 7:
        answer[0] = 6
    if answer[1] >= 7:
        answer[1] = 6
    # answer.sort()
    return answer


def solution2(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans], rank[ans]


def solution3(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]
