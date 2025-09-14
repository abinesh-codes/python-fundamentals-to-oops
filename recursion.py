# Factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n* factorial(n-1)
n = 5
print([factorial(i) for i in range(n + 1)])

# Fibonacci using recursion
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return  1
    else:
        return Fibonacci(n-1) + Fibonacci(n -2)

n = 10
series = [Fibonacci(i) for i in range(n + 1)]     
print(series)

# Tail & Non-Tail recursion

def tail(n,acc = 1):
    if n == 0 :
        return acc
    else:
        return tail(n-1,acc *n)

def non_tail(n):
    if n == 0:
        return 1
    else:
        return n *non_tail(n-1)

print(tail(5))
print(non_tail(6))