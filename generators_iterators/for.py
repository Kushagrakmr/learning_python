def my_for(iterable):
    k = iter(iterable)
    while True:
        try:
            print(k.__next__())
        except StopIteration:
            break


my_for("kush")
my_for([34,4,32,2,245,5,6,6,3,4,54,35,32,4,3,4,24,23])