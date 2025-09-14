#  Counter 

from collections import Counter

# Basic 
li = [2,2,3,4,5,5,3,4,3,3,1,1,1,7,8,8,7]
count_li = Counter(li)
print(count_li)

# Accessing Element in Counter

print(count_li[3])
print(count_li[2])
print(count_li[9]) # if the Element ! in Counter than return 0

# Update Elements in Counter

count_li.update([9,9,9,00,00,00,999,999])
print("Updated Values:",count_li)

# Counter Methods
# elements()

count_element = Counter({"app":5,"Web":6})
items = list(count_element.elements())
print(items)

# most_common()
item = Counter([11,22,33,33,22,33])
items = item.most_common()
itemss = item.most_common(2) # This give 2 value of the counted items
print(items,"\n",itemss)

# Subtract()
list1 = Counter([1,2,2,3,3,3,4,4,4,4])
list2 = Counter([1,2,3,4])
list1.subtract(list2)
print(list1)

# Arithmatic Operation in Counters
list1 = Counter([1,2,2,3,3,3,4,4,4,4])
list2 = Counter([1,1,2,2,3,3,4,4])

print(list1 + list2)
print(list1 - list2)
print(list1 & list2)
print(list1 | list2)
