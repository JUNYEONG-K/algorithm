import heapq


# 오름차순 힙 정렬 (Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)    # value 대신 -value => 내림차순
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h)) # heap~ 대신 -heap => 내림차순
    return result


def main():
    result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    print(result)


main()