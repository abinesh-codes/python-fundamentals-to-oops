# Sample

class Dog:
    def __init__(self,name,age,breed):
        self.name = name
        self._breed = breed
        self.__age = age

    def get_info(self):
        return f"DOG NAME:{self.name} , BREED :{self._breed} , AGE : {self.__age}"

    # Getter & Setter Method Involved
    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid Input")
dog = Dog("Husky",2,"Huskimo")

print(dog.name)
print(dog.get_age())
dog.set_age(5)
print(dog.get_info())