from collections import Counter
num = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
cnt = Counter(num)
print(cnt)
cnt1 = Counter("Hello")
print(cnt1)

class cat:
    # Class variable
    species = "Canine"
    def __init__(self, name, age):
       # Instance variables
        self.name = name
        self.age = age
# Create objects
cat1 = cat("Buddy", 3)
cats2 = cat("Charlie", 5)

# Access class and instance variables
print(cat1.species)  # (Class variable)
print(cat1.name)     # (Instance variable)
print(cats2.name)     # (Instance variable)
# Modify instance variables
cat1.name = "Max"
print(cat1.name)     # (Updated instance variable)

# Modify class variable
cat.species = "Feline"
print(cat1.species)  # (Updated class variable)
print(cats2.species)
class cat:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

# Example Usage
dog = cat("Buddy", "Labrador", 3)
# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class

# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())

"""
Inheritance
"""
#1. Using the super() method
class Animal:
    def __init__(self, name):
        self.name = name
    def info(self):
        print("Animal Name: ", self.name)

#Child class : Dog
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) #Call the constructor of the parent class
        self.breed = breed
        