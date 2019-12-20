# raise ValueError("Invalid Value")
# raise ValueError
# raise NameError("Hello")

def colorize(text, color):
    colors = ("cyan", "yellow", "green", "blue", "magenta")
    if type(text) is not str:
        raise TypeError("The text must be an instance of string")
    if color.lower() not in colors:
        raise Exception(f"The value of color must be {colors}")  
    print(f"Printed {text} in {color}")

colorize("hello", "green")
# colorize(5, "gray")
colorize("heoo", "gray")
colorize(5, "hs")