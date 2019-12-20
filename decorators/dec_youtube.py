def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a, b): #Same parameter as div
        if a < b :
            a, b = b, a

        return func(a,b)
    
    return inner


new_div = smart_div(div)
new_div(5,2)
div(5,2)
print()
print()
new_div(2,5)
div(2,5)
