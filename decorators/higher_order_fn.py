from random import choice

def greet(person):
    def get_mood():
        msg = choice(("Hello there", "Go away", "fuck off", "Miss you", "It's boring"))
        return msg

    result = get_mood() + person
    return result

print(greet(" Kushagra"))


# We can pass the functions as an argument 

def sum(n, func):
    total = 0
    for num in range(n):
        total += func(num)

    return total

def square(x):
    return x*x

def cube(x):
    return x*x*x

print(sum(5, square))
print(sum(4, cube))