# greedy
def solution(n, lost, reserve):
    answer = 0
    # 여벌 옷을 가져온 학생도 도난을 당했을 수 있다는 전제가 있다.
    # 따라서 중복되는 학생은 각 집단에서 제거해줄 것이다. (고려하지 않을 것)
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for p in set_reserve:
        if p-1 in set_lost:
            set_lost.remove(p-1)
        elif p+1 in set_lost:
            set_lost.remove(p+1)
    answer = n - len(set_lost)
    return answer
