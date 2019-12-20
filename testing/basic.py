# def add_positive_numbers(x, y):
#     assert x > 0 and y > 0, "Both numbers must be positive!"
#     return x + y

# print(add_positive_numbers(23,41))
# print(add_positive_numbers(-23,41))

def eat_junk(food):
    assert food in ['pizza', 'ice cream', 'candy', 'burger'], "This is a fast food"
    return f"Hey, I'm eating {food}"

food = input("Enter a food ")
print(eat_junk(food))