days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
# list of same type (mutable)
# Python Standard Library -> many kinds of func or operator
print(days)
print(type(days))
print("Mon" in days)    # True -> 'in' operator response bool
print(days[3])  # index start from 0
print(len(days))
days.append("Sat")  # add value in end of list
days.append("SUn")
print(days)
days.pop()
print(days) # remove end of list (add in latest)
days.reverse()
print(days)
print(days[1:]) # index 1번부터의 배열
print(days[1:4]) # index 1번부터 4번까지의 배열
print(days[:4]) # index 0번부터 3번까지의 배열
days.sort(reverse=True)