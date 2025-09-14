n = [2,3,4,5,6,8,9]

# map
sq =list(map(lambda x:x*x,n)) 
print(sq)

#filter 
odd = list(filter(lambda x:x%2==1,n))
print(odd)

#sorted
#easy way
pair = [(3, 'three') ,(2, 'two'), (1, 'one')]
sort = sorted(pair,key=lambda x: x)
print(sort)


#another way
pairs = [(1, 'a'), (3, 'c'), (2, 'b')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# reduce
from functools import reduce

tot = reduce(lambda x,y : x+y,n)
print(tot)

# Upper case 
S = "hello World"
s = lambda x: x.upper()
print(s(S))


# Lambda() for the conditional Statement
n = int(input("Enter a Number:"))
f = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(f(n))

# List Comprehension
li =  [lambda a=x : a*10 for x in range(1,6)]
for i in li :
    print(i())

#if else
f = lambda x : "even " if x%2 ==0 else "odd"
print(f(10))


# Multiple Statements

f = lambda x ,y : (x+y ,x-y)
print(f(8,2))