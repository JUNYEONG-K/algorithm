def solution(phone_book):
    # for num1 in phone_book:
    #     for num2 in phone_book:
    #         if num1 == num2:
    #             continue
    #         else:
    #             if num1 in num2 or num2 in num1:
    #                 return False
    # return True

    # for i in range(len(phone_book)):
    #     for j in range(i):
    #         if phone_book[i] in phone_book[j] or phone_book[j] in phone_book[i]:
    #             return False
    # return True

    phone_book.sort()
    # for i in range(len(phone_book)):
    #     for j in range(i):
    #         if phone_book[i].startswith(phone_book[j]):
    #             return False
    # return True

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


