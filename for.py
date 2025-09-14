# Normal For Loop Concept
num =4 
for i in range(2,num):
    print(i)


# List, Tuple, String, and Dictionary Iteration  using string in for loop

li = ["geeks", "for", "geeks"]
for i in li:
    print(i)
    
tup = ("geeks", "for", "geeks")
for i in tup:
    print(i)
    
s = "Geeks"
for i in s:
    print(i)
    
d = dict({'x':123, 'y':354})
for i in d:
    print("%s  %d" % (i, d[i]))
    
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i)

# Iteration using Index sequence

li = ["appple" , "banana", "cherry"]
for i in range(len(li)):
    print(li[i])

# using Else statement in for loop 

num =[2,4,6,8,10]
for i in num:
    if i == 5:
        print("Found")
        break
else:                    # The else block runs only if the for loop completes normally — i.e., without hitting a break statement.
    print("Not Found")