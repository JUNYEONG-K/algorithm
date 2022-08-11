# 원소가 최대 100,000 개까지 입력될 수 있으므로 최악의 경우에도 O(NlogN)인 정렬 알고리즘 사용하여야 함 (O(N^2) 이면 시간초과 뜰 수 있음)
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i] = B[i]
    else:   # break 문 꼭 필요한가? 내가 짠 코드는 else 문 빼고 다 똑같음
        break

print(sum(A))