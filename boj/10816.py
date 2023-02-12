_ = input()
N = map(int, input().split())
_ = input()
M = map(int, input().split())
hashmap = {}
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1
print(hashmap)
print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))