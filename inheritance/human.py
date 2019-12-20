class Human:

    def __init__(self, first, last, age):
        self.first = first
        self.last  = last
        self._age = max(age, 0)

    # def get_age(self):
    #     return self._age

    # def set_age(self, age):
    #     self._age = max(0, age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = max(value, 0)
    
    @property
    def full_name(self):
        return f"{self.first} {self.last}"


    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")


kush = Human("Kushagra", "Kumar", 22)