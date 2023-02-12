from collections import deque


def solution(people, limit):
    people.sort()
    q = deque(people)
    boat = 0
    while q:
        if len(q) > 1:
            if q[0] + q[-1] <= limit:
                q.popleft()
                q.pop()
                boat += 1
            else:
                q.pop()
                boat += 1
        else:
            q.pop()
            boat += 1
    return boat
