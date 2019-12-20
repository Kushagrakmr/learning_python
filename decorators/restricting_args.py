from functools import wraps

def ensure_first_arg_is(val):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] is not val:
                return(f"The first item should be {val}")
            return func(*args, **kwargs)

        return wrapper
        
    return inner




@ensure_first_arg_is("pizza")
def fav_foods(*foods):
    print(foods)

print(fav_foods("pizza", "cake"))
print(fav_foods("icecream", "pizza", "cake"))


@ensure_first_arg_is(10)
def add_ten(num1, num2):
    return num1 + num2

print(add_ten(23, 51))
print(add_ten(10, 34))