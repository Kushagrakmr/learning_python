import time


def performance(func):
    def inner(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(func.__name__ + "took " + str((end-start)*1000) + " milli seconds")

        return result

    return inner

@performance
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)

    return result

@performance
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)

    return result










array = range(1, 1000000)
out_square = calc_square(array)
out_cube = calc_cube(array)



