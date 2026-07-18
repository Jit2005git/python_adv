class InvalidAgeError(Exception):
    pass
def check_age(age):
    if age<18:
        raise InvalidAgeError("Age must be at least 18 or above")
    print("Age is valid")
check_age(15)