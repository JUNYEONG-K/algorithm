from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    # 중복 신고 제거
    report = list(set(report))
    # user별 신고한 id 저장
    user = defaultdict(set)
    # user별 신고당한 횟수 저장
    cnt = defaultdict(int)

    for r in report:
        # report의 첫번째 값은 신고자id, 두번째 값은 신고당한 id
        a, b = r.split()
        # 신고자가 신고한 id 추가
        user[a].add(b)
        # 신고당한 id의 신고 횟수 추가
        cnt[b] += 1
    print(user)
    print(cnt)
    for i in id_list:
        result = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)
    return answer


def solution2(id_list, report, k):
    answer = [0] * len(id_list)
    # 유저 별로 신고 당한 횟수를 기록하기 위한 사전 자료형
    reports = {x: 0 for x in id_list}  # {'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0}

    # 유저 별로 신고 당한 횟수를 기록
    for r in set(report):
        reports[r.split()[1]] += 1

    # 메일 수신 횟수 기록
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
