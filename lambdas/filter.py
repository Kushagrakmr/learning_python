names = ["Kushagra", "Rimmi", "Golu", "Ankit", "Indiver", "Gaurav", "Gautam"]

a_names = filter(lambda name :  name[0] == 'A', names)
list(a_names)


list(map(lambda name: f"This pc belongs to {name}" ,filter(lambda name: len(name) > 7, names)))