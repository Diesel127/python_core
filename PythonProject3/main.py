class ApplicationError(Exception):
    pass
class ValueTooLargeError(ApplicationError):
    pass
class NegativeValueError(ApplicationError):
    pass

def check_number(value):
    if value < 0:
        raise NegativeValueError("Value is negative")
    elif value > 100:
        raise ValueTooLargeError("Value is too large")
    else:
        return "The value is acceptable."
try:
    num = int(input())
    print(check_number(num))
except NegativeValueError as e:
    print(f"Error: {e}")
except ValueTooLargeError as e:
    print(f"Error: {e}")
except ApplicationError as e:
    print(f"An application error occurred: {e}")