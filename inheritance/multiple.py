class Aquatic:
    def __init__(self, name):
        print("Aquatic INIT")
        self.name = name

    def swim(self):
        return f"{self.name} is swimming."

    def greet(self):
        return f"I am {self.name} of the sea!"


class Ambulatory:
    def __init__(self, name):
        print("Ambulatory INIT")
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"


class Penguin(Aquatic , Ambulatory):
    def __init__(self, name):
        print("Penguin INIT")
        super().__init__(name=name)

# class Penguin(Ambulatory, Aquatic):
#     def __init__(self, name):
#         print("Penguin INIT")
#         Aquatic.__init__(self, name=name)
#         Ambulatory.__init__(self, name=name)


cc = Penguin("Captian Cook")
print(cc.greet())