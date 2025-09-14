# Normal Local & Global variable
def func():
    x =5 
    print(x)

x = 10
print(x)
func()


# Modifying Global Variable inside a function
def fun():
    global x
    x += " Guys"  # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value ,If we don't declare x as global
    print(x)

x = "Vanakam"
fun()

# Example of Global Variable

a = 1  # Global variable

def f():
    print('f():', a)  # Uses global a

def g():
    a = 2  # Local variable shadows global
    print('g():', a)

def h():
    global a
    a = 3  # Modifies global a
    print('h():', a)

print('global:', a)  
f()                  
print('global:', a) 
g()                 
print('global:', a)  
h()                  
print('global:', a)