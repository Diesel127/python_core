class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age > 150:
        raise InvalidAgeError("Age cannot be greater than 150.")

try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Age is valid.")
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Please enter a valid integer for age.")
