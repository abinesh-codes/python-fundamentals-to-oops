# Basic Filter example
a = [1, 2, 3, 4, 5,6]
def odd(n):
    return n % 2 == 1
filtered =list(filter(odd,a))
print(filtered)

#lambda 
fil = list(filter(lambda x: x%2 == 0 , a ))
print(fil)


# Combining filter() with Other Functions
filt = list(map(lambda x:x*2,fil))
print(filt)