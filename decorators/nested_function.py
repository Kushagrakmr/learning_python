def outer():
    print("Outer function execution")

    def inner():
        print("Inner function execution")

    print("Returning inner function")

    return inner

k = outer()

