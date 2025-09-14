# Methods of Adding a element into the list 

a =[]
a.append(30) # Add

a.insert(0 , 15) # Insert

a.extend([45,60,75]) # Extend

print(a)

# Methods of Removing a element from the list 

a.remove(60) # Remove
print(a)

a.pop() # Pop
print(a)

del a[2] # Delete Statement
print(a)


# List Comprehension
values = [(x,y) for x in range(4) for y in range(2)] # nested loop
print(values) # [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)]

a = [[1,2,3],[4,5,6],[7,8,9]]  # Converting a list of lists into a single list
res = [x for y in a for x in y]
print(res)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = [1,3,5,6,8,763,8,67,554646,4,4] # Conditional Statement
count = [x for x in a if x % 2 == 0]
print(count)