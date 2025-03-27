# age : int
# name: str
# height: float


# in age, we are declaring the input type as int and in -> we are declaring the output type
def police_check(age: int) -> bool:

    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive
