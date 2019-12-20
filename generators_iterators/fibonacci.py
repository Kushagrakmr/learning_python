def fibo(n):
    count = 1
    a, b = 0, 1
    while count < n:
        a, b = b, a+b
        yield a
        count += 1


k = fibo(15)
while True:
    try:
        print(next(k))
    except StopIteration:
        break