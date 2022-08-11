def say_hello(name, age):
    print("hello " + name)    # end = '\n' (basic)
    print(f"{name} is {age} years old")  # 문자열에 변수를 삽입하는 최신 방법
# 들여쓰기 필수, 이는 함수를 구분하기 위한 수단으로 타언어에서는 주로 중괄호{}를 쓴다.


def basic_func():
    # basic python built-in-function is very very many
    num = "18"  # str
    print(type(num))
    n_num = int(num)  # to str
    print(n_num)  # int
    print(type(n_num))


def plus(a, b):
    print(a+b)
    return a+b
    print("return kill the function")


def minus(a, b=3):  # b has default value 3
    print(a-b)
    return a-b


def none():
    print("it's none")


# others are sequence arg
def keyword_arg(first, second):
    return f"first is {first} and second is {second}"


def main():
    name = "jun"
    age = 23
    say_hello(name, age)    # () is necessary
    plus_result = plus(2, 4)
    print(f"plus result = {plus_result}")
    minus_result = minus(5)
    print(f"minus result = {minus_result}")
    minus(5, 1)     # change second value from 3 to 1
    print(none())   # None
    print(keyword_arg(second=2, first=1))
    basic_func()


main()

