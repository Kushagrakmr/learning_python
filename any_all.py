# Returns if all the values in the iterable is truthy

all([2,4,50,35])

names = ["Anom", "Anker", "Anit", "Ather"]
all([name[0] == "A" for name in names])

names.append("HEllo")
all([name[0] == "A" for name in names])