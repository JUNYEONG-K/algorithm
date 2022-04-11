array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):   # 인덱스 i 부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1]:   # 한칸씩 왼쪽으로 이동 (내 왼쪽에 있는 원소와 비교)
            array[j], array[j-1] = array[j-1], array[j]
        else:   # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)