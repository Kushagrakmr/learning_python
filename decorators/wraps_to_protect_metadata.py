from functools import wraps
def log_function_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """I am the wrapper function"""
        print(f"You are about to call {func.__name__}")
        print(f"Here's the documentation: {func.__doc__}")

        return func(*args, **kwargs)

    return wrapper


@log_function_data
def add(x, y):
    """Adds two numbers together"""
    return x+y


print(add(23,32))

