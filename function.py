def evenodd(x: int) -> str:
    if x% 2 ==0:
        return "Even"
    else:
        return "Odd"

print(evenodd(18))
print(evenodd(5))


#Document String 
def evenodd(x):
    """Function to check if the number is even or odd""" # with the help of the __doc__ is used to print the docstring of the function
    
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


print(evenodd.__doc__)