# Set DataType

s = {1,2,5,8,7,4,6,9,9,8,2,"python","py"}
print(s)
print(type(s))

# Adding & Removing Elments
s.add("Flask")
s.remove("py")
s.discard("python")

print(s,end="\n\n")

# Set Operations
a={1,2,3}
b={3,4,5}

print(a|b)
print(a&b)
print(a-b)
print(a^b)