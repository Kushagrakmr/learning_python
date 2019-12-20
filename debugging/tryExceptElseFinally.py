try:
    num = int(input("Please enter a number  "))
except ValueError as err:
    print("That is not a number")
    print(err)
else:
    print("This is coming from the else")
finally:
    print("This is going to be printed anyhow.")