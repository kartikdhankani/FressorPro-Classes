# Date - 25.05.2025 
#Day - Sunday
# Time - 10:00 AM

#list function using "[ ] " brackets
# You can have any data like strings or integers in a list
# stocks - AAPL, AMZN, CIPLA, SBIN
stocks = ['AAPL', 'AMZN', 'CIPLA', 'SBIN']
# indexing = [ 0,1,2,3]
a=[22,33,44,55]
#a[0] will give you first element of the list, and there on. 
# -1 will give last data, -2 will give last second data and there on.
a[1]
a[-1] # will give you last element of the list
a[-1]
a[1:3] # will give you 2nd and 3rd element of the list
a[1:3]

print(a[1:3])

# append function is used to add new element to the list
a.append(66)
a.append(77)
a.append(88)

#insert function is used to add new element at a specific index
#insert will add an element with an index/position value

a.insert(2, 99)  # This will insert 99 at index 2
a.insert(1,110)

#remove function is used to remove an element from the list
a.remove(44)

#pop fiction is used to remove the last element from the list
a.pop()  # This will remove the last element (88 in this case)
print(a)

a1=a

a1.pop(4)  # This will remove the element at index 4, which is 110
print(a1)

a2=a1

a2.append(220)  # This will add 220 to the end of the list
print(a2)

#del function is used to delete the entire list or mention an index

del a2[4]  # This will delete the element at index 4
print(a2)

a3=a2

print(a3)

del a3[2]  # This will delete the element at index 2
print(a3)

a4=a3
a4.remove(99)  # This will remove the element 99 from the list
print(a4)

"python".index("t")  # This will return the index of the first occurrence of 't' in "python"
# python is a string here.

s='python'
s.replace('y'.'o')

#You can not update a string, but you can create a new string with the updated value
#You can update a list, but you can not update a string : Use list.replace['replace value','new value']

s1=s.replace('y', 'o')  # This will create a new string with 'y' replaced by 'o'
print(s1)  # Output: 'pothoon'

# Use square bracket [] for indexing and slicing
# Use round brackets () for functions and methods




