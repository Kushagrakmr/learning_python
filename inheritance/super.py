class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species
         
    def __repr__(self):
        return f"{self.name} is a {self.species}"
        
    def make_sound(self, sound):
        print(f"The {self.name} says {sound}")
    

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species = "Cat")


        # In here the animal class has name and species so there is no point in specifying this again here. 

        #Here's another way of doing this. One other way is the one which is used here.
        # Animal.__init__(self, name, species)

        # self.name = name
        # self.species = species

        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")

    



blue = Cat("Blue", "Scottish Fold", "Woolen Ball")
print(blue)