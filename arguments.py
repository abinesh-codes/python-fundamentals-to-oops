#Default Argument

def fun(x = 10):
    return x
print(fun(5))
print(fun())

#Keywrod Argument

def func(fname,lname):
    return fname+" weds " + lname
print(func(fname = "A",lname ="B"))
print(func(lname = "B",fname ="A"))

#Positional Argument
def func (name,age):
    return name ,"is ",age,"years old"  #If you want to use the + instead of the comma means you have to convert the integer input to string by str(age)
print(func("A",35))
print(func(35,"A"))

# TypeError: can only concatenate str (not "int") to  must be clear
def func(name, age):
    return str(name) + " is " + str(age) + " years old"
print(func("A", 35))    
print(func(35, "A"))    

# Arbitrary Keywrod Argument
# *args
def func(*args):
    for i in args:
        print(i)
func("Hello ","Guys","Welcome","to ","Python")

# **kwargs
def func(**kwargs):
    for key,value in kwargs.items():
        print(key," == ", value)

func(face="book",insta="gram",you="tube")