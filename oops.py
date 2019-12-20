class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make= make
        self.price =price
        self.on = False
        
    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", "9.99")
print(kenwood.price)
print(kenwood.make)

kenwood.price = 12.55
kenwood.price


milton = Kettle("Milton", "33.45")
print(milton.make)
print(milton.price)


print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(milton, kenwood))

milton.switch_on()

Kettle.switch_on(kenwood)
kenwood.switch_on()

print("Switching to atomic power")
Kettle.power_source = "Atomic"

print("Switching kenwood to gas")
kenwood.power_source = "Gas"

print("*"*20)
kenwood.power = 1.5 
print(kenwood.power)
# print(milton.power)

print(Kettle.power_source)
print(milton.power_source)
print(kenwood.power_source)

print(Kettle.__dict__)
print(milton.__dict__)
print(kenwood.__dict__)
