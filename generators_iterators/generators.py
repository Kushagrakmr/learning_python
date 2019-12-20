def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1



k = count_up_to(20)
while True:
    try:
        print(next(k))
    except StopIteration:
        break