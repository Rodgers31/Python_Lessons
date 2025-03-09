# with the asterisk key work, we are able to send as many arguments to the function as we want
def add(*args):
    print(args[0])
    num_sum = 0
    for i in args:
        num_sum += i
    return num_sum


result = add(5, 7, 8, 20, 45, 99, 193, 45)
print(result)

# Adding key word to your function
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        # get will make the code not fail even if the value is not passed
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)