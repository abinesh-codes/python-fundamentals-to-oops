# basic inner function 
def func(msg):
    def fun():
        print(msg)
    fun()
func("Hello World")

# Local varibale access
def outer():
    msg = "python"
    def inner():
        print(msg)
    inner()
outer()

# Modifying outer variable  using nonlocal 
def outer():
    msg = "python"
    def inner():
        nonlocal msg
        msg ="nohtyp"
    inner()
    return msg
print(outer())

# Closure 
def outer(a):
    def inner():
        return a * 2
    return inner

f = outer(9)
print(f())

# Real - World Applications of inner functions
def outer(data):
    def inner():
        return [item.strip() for item in data]
    return inner()

data = ["     apple      ", "     banana      ", "       cherry       "]
print(outer(data))