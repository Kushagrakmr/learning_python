class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"The no. of active users are {cls.active_users}"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, age)

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = max(age, 0)
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"The {self.first} has logged out."

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, item):
        return f"{self.first} likes {item}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday, {self.first}"


class Moderator(User):
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community."


kush = Moderator("Kushagra", "Kumar", 22, "Python")
print(User.active_users)
u1 = User("Rimmi", "Hazari", 20)
print(User.active_users)