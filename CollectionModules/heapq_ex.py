# heapq
 
import heapq

# Basic 

li = [10,20,30,5,15,25]
heapq.heapify(li) # Convert the list into Valid Heap 
print(li) 

# Insert a new value

heapq.heappush(li,35)
print(li)

# Remove & Return a value

min = heapq.heappop(li)
print("Smallest: ",min)
print(li)

# Insert and Remove a value 

heapq.heappushpop(li,40)
print(li)

# Find Maximum Value in li

large = heapq.nlargest(3,li)
print(large)

# Find Maximum Value in li

small = heapq.nsmallest(3,li)
print(small)

# Replace heap

remove = heapq.heapreplace(li,45)
print(remove)
print(li) # In this the smallest value will removed and the new value is add into the heap

# Merge

li1 =[1,3,5,7,9]
li2 =[2,4,6,8,0]

merged = heapq.merge(li1,li2)
print(list(merged))