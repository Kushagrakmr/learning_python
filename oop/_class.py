class User:

    active_users = 0

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


kush = User("Kushagra", "Kumar", 23)
print(kush.logout())
print(kush.initals())