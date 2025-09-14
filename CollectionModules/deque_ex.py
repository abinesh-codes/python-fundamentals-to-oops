# deque

from collections import deque

d = deque(['name','age','dob'])
print(d)

# Rotate 
de = deque([1,2,3,4,5])
de.rotate(-3)
print("After rotated the deque",de)

de.rotate(2)
print("After rotated the deque",de)

de.rotate(4)
print("After rotated the deque",de)

# Normal Operations

dq = deque([10,20,30,40])

dq.append(50)
print("After a value added to right end :",dq)

dq.appendleft(5)
print("After a value added to left end:",dq)

dq.pop()
print("After a value removed to right end:",dq)

dq.popleft()
print("After a value removed to left end:",dq)

dq.extend([55,60,65])
print("After a value added to right end:",dq)

dq.extendleft([15,25,35])
print("After a value added to left end:",dq)

print("Removed a Specfic value from deque:",dq.remove(55))

dq.reverse()
print("Reversed Deque:",dq)

print("Index of the Specfic value :",dq.index(60))

print("Count the repeated value of the No:",dq.count(30))

dq.clear()
print("Empty ",dq)