n, m = map(int, input().split())

no_listen = set()
no_seen = set()
for _ in range(n):
    no_listen.add(input())
for _ in range(m):
    no_seen.add(input())

# 집합 자료형 set 지렸다...
result = sorted(list(no_listen & no_seen))
print(len(result))
for i in result:
    print(i)

