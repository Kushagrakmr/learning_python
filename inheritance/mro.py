#Method Resolution Order

class A:
    def do_something(self):
        print("Method Defined In: A")

class B(A):
    def do_something(self):
        print("Method defined In: B")

class C(A):
    def do_something(self):
        print("Method defined In: C")

class D(C, B):
    # def do_something(self):
    #     print("Method defined In: D")

thing = D()
thing.do_something()

