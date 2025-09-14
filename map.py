#basic map function example
a = [1, 2, 3, 4, 5]

def sq(x):
    return x ** 2

squared = list(map(sq, a))
print(squared)

# with lambda
sqr  = list(map(lambda x : x ** 2, a))
print(sqr)

#Multiple Arguments
a = (2,3,4,5,8) 
b = (9,7,5,3,2)
c = list(map(lambda x,y: x+y ,a,b))
print(c)

# Extracting first character from strings
word = ('apple','banana','cherry')
res = list(map(lambda x : x[0],word))
print(res)

# temperature conversion
celsius = [20,55,36,44,25]

f = list(map(lambda x: (x*9/5)+32 , celsius))
print(f)

fahrenheit = [68.0, 131.0, 96.8, 111.2, 77.0]
c = list(map(lambda y: (y-32)*5/9,fahrenheit))
print(c)