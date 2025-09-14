# This is an example of using the self parameter in a class in Python
class sample:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        return f"MY name is {self.name} and i am {self.age} years old"

show = sample('abi',20)
print(show.display())

# To find area of a circle using class 
class circle:
    def __init__(self,r):
        self.r = r
    
    def area(self):
        return 3.14 * self.r**2

area_circle =circle(int(input("Enter the Radius:")))
print(f"Area of a circle is {area_circle.area()}")