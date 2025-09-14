# Basic Problem 
dic = {1 : "a", 2 : "b" , 3 : "c"}
print(dic[2])
print(dic.get(3))

# Adding & Updating
d = {"name": "Alice", "age": 30, "city": "New York"}

d["pin"] = 666554
d["name"] = "Paithiyam"

print(d) #{'name': 'Paithiyam', 'age': 30, 'city': 'New York', 'pin': 666554}

#Removing the items
del d["pin"]
print(d)

val = d.pop("age")
print(val)

key, value = d.popitem()
print(f"key = {key} value = {value}")

d.clear()
print(d)

# Using loop
dic = {
    "fruit": "apple",
    "quantity": 5,
    "price": 10.5
}
for key in dic:
    print(key)

for value in dic.values():
    print(value)
for key, value in dic.items():
    print(f"{key} :: {value}")


# Nested Dictionary
d = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

print(d)

# Copying Methods
import copy

original = {'name': 'Alice', 'marks': {'math': 90, 'science': 9 }}
print(original)

shallow = copy.copy(original)
shallow["marks"]["math"] = 100
print(shallow)


originals = {'name': 'Alice', 'marks': {'math': 60, 'science': 9 }}
print(originals)
deep = copy.deepcopy(original)
deep["marks"]["math"] = 80
print(deep)