# Run it in administrator mode
# python -m doctest -v doctest_demo.py
def add(x, y):
    """add together x and y
    >>> add(1, 2)
    3

    >>> add(100, 10)
    1010

    """
    return x + y

# a, b = list(map(int, input().split()))
# print(add(a, b))