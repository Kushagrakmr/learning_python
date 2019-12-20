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


# kush = User("Kushagra", "Kumar", 23)
# rimmi = User("Anamika", "Hazari", 22)
# print(User.display_active_users())
# kush = User("Kushagra", "Kumar", 23)
# rimmi = User("Anamika", "Hazari", 22)
# print(User.display_active_users())


golu = User.from_string("Kush,Kumar,45") # Calls the class method
