# sorting
n = int(input())
cranes = list(map(int, input().split()))

m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if max(boxes) > max(cranes):
    print(-1)
else:
    time = 0

    while boxes:
        if not boxes:
            break

        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        time += 1

    print(time)
