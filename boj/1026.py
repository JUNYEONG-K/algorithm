# greedy, sort
n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

result = 0

for i in range(n):
    result += a[i] * b[i]

# 배열을 재배열하지 않고, 그 당시 배열에 존재하는 최대값과 최소값을 곱해서 더해준 후 pop 을 이용해서 배열에서 없애는 방식!
# n = int(input())
#
# a_list = list(map(int, input().split()))
# b_list = list(map(int, input().split()))
#
# s = 0
# for i in range(n):
#     s += min(a_list) * max(b_list)
#     a_list.pop(a_list.index(min(a_list)))
#     b_list.pop(b_list.index(max(b_list)))
#
# print(s)
print(result)