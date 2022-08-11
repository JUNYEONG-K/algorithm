# greedy

n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))  # coin[i] = int(input()) => index error 왜냐면 coin은 빈배열이니까!
coin.sort(reverse=True)
count = 0

for i in range(n):
    count += k // coin[i]  # k 보다 coin이 크면 어차피 0 임
    k = k % coin[i]  # k에서 coin을 뺄 수 있는만큼 여러번 빼고 남은 값

print(count)