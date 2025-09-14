# OrderedDict
from collections import OrderedDict

od = OrderedDict()
od['apple']=1
od['Banana']=2
od['Gava']=3

print(list(od.items()))

# Insert the Values in OrderedDict
d = {'a':1 , 'b':2 , 'c':3}

for k,v in d.items():
    print(k,":",v)
print("OrderedDict ")
od= OrderedDict([('d',4),('a',1),('b',2),('e',5),('c',3)])
for k,v in od.items():
    print(k,":",v)

# Changing value does not affect order
print("Changed")
od['e'] = 7
for k,v in od.items():
    print(k,":",v)

# Equality checks consider order
od1 =  OrderedDict([('d',4),('a',1),('b',2),('e',5),('c',3)])
od2 =  OrderedDict([('a',1),('b',2),('d',4),('c',3),('e',5)])
print(od1 == od2)

# Reverse the OrderedDict
d1 =  OrderedDict([('d',4),('a',1),('b',2),('e',5),('c',3)])
d2 = OrderedDict(reversed(list(d1.items())))
print(list(d2.items()))

# popitems
d1 =  OrderedDict([('d',4),('a',1),('b',2),('e',5),('c',3)])
d1.popitem(last=True)
d1.popitem(last=False)
print(d1.items())

# Move to end 
dic =  OrderedDict([('d',4),('a',1),('b',2),('e',5),('c',3)])
dic.move_to_end('d',last = True)
dic.move_to_end('e',last = False)
print(list(dic.items()))

