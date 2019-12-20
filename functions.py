#  *args
def sum_all_nums(*nums):
    print(nums)
    sum = 0
    for num in nums:
        sum += num
    
    return sum

# print(sum_all_nums(4,563,3,24,543))


# **kwargs  # Gathers the remaining arguments as dictionary
def fav_colour(**kwargs):
    print(kwargs)
    print(kwargs.values())
    print(kwargs.keys())
    for values in kwargs.items():
        print(values[0] + " fav_color is " + values[1])


# fav_colour(kush="blue", Rimmi="yellow", golu="grey")

# Parameter ORdering
# 1. Parameters
# 2. *args
# 3. default Parameters
# 4. **kwargs

