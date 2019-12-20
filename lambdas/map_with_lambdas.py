nums = list(range(0,20))
nums

even = map(lambda a: a*5, nums)
list(even)

names = ["Kushagra", "Rimmi", "Golu", "Ankit", "Indiver", "Gaurav", "Gautam"]

upper_names = list(map(lambda name: name.upper(), names))
upper_names