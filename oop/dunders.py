class User:
    active_users = 0

    @classmethod
    def  display_active_users(cls):
        return f"There are currently {cls.active_users} acitve users at the moment."

    @classmethod
    def from_string(cls, data_string):
        first, last, age = data_string.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    # This is just like operator overloading. Here we are overloading the output operator to reperesent the class
    def __repr__(self):
        return f"{self.first} is {self.age}"
    
    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initals(self):
        return f"{self.first[0]}.{self.last[0]}"
    
    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65


kush = User("Kushagra", "Kumar", 23)
rimmi = User("Anamika", "Hazari", 22)

g = User("Golu", "Singh", "34")
print(g)
print(str(g))
