# Basic Class and Object
class Dog:
    species = "Husky" # Class Attribute

    def __init__(self,name,age):
        self.name = name #Instance Attribute
        self.age = age #Instance Attribute

dog = Dog("Bubble",2)

print(dog.name)
print(dog.species)

print(Dog.species)

# Sample 2

class Dogs:
    species = "Harry"
    def __init__(self,name,age):
        self.name = name
        self.age = age
dog1 = Dogs("Gopal",2)
dog2 = Dogs("Ranji",4)
dog3 = Dogs ("Rajan",2)


print(dog1.name,dog1.age,dog2.name)
print(dog2.age,dog3.name,dog1.name)
print(dog3.name,dog2.age,dog1.name)

# Self Parameter
class demo:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def std(self):
        print(f"{self.name} is Studying well")

    def stdd(self):
        print(f"{self.name} is not studying well")

std1 = demo("Abi",20)
std2 = demo("Ranji",17)

std1.std()
std2.stdd()

# __str__() Method

class sample:

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"{self.name} is front-end developer and his age is{self.age}")

user = sample("Abinesh",20)

print(user)

# without __str__() Method
class sample:

    def __init__(self,name, age):
        self.name = name
        self.age = age

users = sample("Abinesh",20)

print(users) # the output will be the <__main__.sample object at 0x0000024BD23F74D0>


# Getter and Setter Method

class example:

    def __init__(self,name):
        self.__name = name
    # Getter
    def get_name(self):
        return self.__name
    #Setter
    def set_name(self,new_name):
        self.__name = new_name

person = example("Abinesh-coder")
print(person.get_name())

person.set_name("Ranjitha")
print(person.get_name())

# @property in Getter and Setter
class example:

    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,new_age):
        self._age = new_age

person = example("Gopal",39)
print(person.name,person.age)

person.name = "Rajan"
person.age = 30
print(person.name,person.age)

# Method Overriding

class parent:

    def parent(self):
        print("The parent class")

class child(parent):
    def parent(self):
        super().parent() # The Parent Class is called here
        print("The Child class")

class1 = child()
class1.parent()

# Class Methods
class Dog:
    species = "Canine"  # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def set_species(cls, species_name):  # class method
        cls.species = species_name

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

print(dog1.species)
Dog.set_species("Domestic Dog")
print(dog2.species)

# Static Methods

class MathUtils:
    @staticmethod
    def add(a, b):   # static method
        return a + b

print(MathUtils.add(5, 3))  # 8

