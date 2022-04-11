days = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")

for day in days:
    # day = Mon -> day = Tue -> ... day = Sun and end loop
    print(day)

for i in range(5):
    # 0, 1, 2, 3, 4
    print(i, end=", ")
print()
for i in range(2, 5):
    # 2, 3, 4
    print(i, end=", ")
print()
for day in days:
    if day == "Wed":    # 'is' makes error, so I write '=='
        break
    else:
        print(day)
for day in days:
    for c in day:   # str is list also
        print(c)