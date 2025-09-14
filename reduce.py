# Basic  reduce example
from functools import reduce
a = [1, 2, 3, 4, 5]
def add (x,y):
    return x+y
tot = reduce(add,a)
print(tot)

#lambda reduce example
totl =reduce(lambda x,y :x*y ,a)
print(totl)

#using operators
from operator import add, mul , sub 
from functools import reduce

a = [1, 2, 3, 4, 5]
tot =reduce(add,a)
tot =reduce(mul,a)
tot =reduce(sub,a)
print(tot)