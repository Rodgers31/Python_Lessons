# with the asterisk key work, we are able to send as many arguments to the function as we want
def add(*args):
    print(args[0])
    num_sum = 0
    for i in args:
        num_sum += i
    return num_sum


result = add(5, 7, 8, 20, 45, 99, 193, 45)
print(result)
