def int_plus(a, b):
    if type(a) is not int or type(b) != int:  # object comparison ?
        a = int(a)
        b = int(b)
    return a+b


def age_check(age):
    print(f"you are {age}")
    if age < 18:
        print("you can't drink")
    elif age == 18 or age == 19:    # or
        print("you are new to this!")
    elif 20 < age < 25:    # and
        print("you are still kind of young")
    else:
        print("enjoy your drink")


print(int_plus(12, "10"))
age_check(21)



