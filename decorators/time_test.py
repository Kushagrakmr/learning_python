from functools import wraps
import time

def performance(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fun(*args, **kwargs)
        end_time = time.time()
        print(f" The time elapsed: {end_time - start_time}")

        return result
    return wrapper

@performance
def sum_nums(nums):
    return sum(x for x in nums)


k = sum_nums(range(0,200000))
