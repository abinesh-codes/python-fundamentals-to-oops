# DefaultDict
from collections import defaultdict

dic = defaultdict(lambda: "Not Present")
dic['a'] = 1
dic['b'] = 2

print(dic['b'])
print(dic['d'])

# Using the list as a defaultdict
d1 = defaultdict(list)

for i in range(6):
    d1[i].append(i)
print("Dictionary value:" ,d1)

# Using the int as defaultdict
d2 = defaultdict(int)

a = [1,2,2,4,4,4,3,3,3,3,3]

for i in a:
    d2[i] += 1

print("Dictionary Values :", d2)

# Using str as the factory function
sd = defaultdict(str)
sd['greeting'] = 'Hello'
print(sd)

# Python defaultdict Type for Handling Missing Keys  
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

print(d.__missing__('a'))
print(d.__missing__('d'))