#Local Scope

def f():
    x = 20
    print("num:",x)

f()


#Global Scope


a = "Vanakam da"

def f():
    global a
    a= "vanakam da mapla"
    print(a)

f()


print(z)
z=10
del z