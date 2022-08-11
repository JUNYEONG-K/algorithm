# zip 메서드!!
n = int(input())

serial = []
for _ in range(n):
    serial.append(input())

for i in range(n-1):
    for j in range(i+1, n):
        # 짧은 것 먼저
        if len(serial[i]) > len(serial[j]):
            serial[i], serial[j] = serial[j], serial[i]
        elif len(serial[i]) == len(serial[j]):
            suma = 0
            sumb = 0
            for x, y in zip(serial[i], serial[j]):
                if x.isdigit():
                    suma += int(x)
                if y.isdigit():
                    sumb += int(y)
            if suma > sumb:
                serial[i], serial[j] = serial[j], serial[i]
            elif suma == sumb:
                for x, y in zip(serial[i], serial[j]):
                    if x > y:
                        serial[i], serial[j] = serial[j], serial[i]
                        break
                    elif x < y:
                        break

for i in serial:
    print(i)
