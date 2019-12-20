a = list(range(1, 10, 2))
b = list(range(0, 10, 2))

list(zip(a, b))
zipper = dict(zip(a,b))

for a in zipper.keys():
    print(a)

midterms = [80, 91, 78]
finals = [90, 94, 53]

students = ["Kush", "Rimmi", "Hey"]

dict(zip(students, [max(pair) for pair in zip(midterms, finals)]))

dict(zip(students, map( lambda pair: max(pair),  zip(midterms, finals))))

