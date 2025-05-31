#Class Date = 31.05.2025
# Class Day = Saturday
# CLass Time = 4:30 PM to 6:30 PM

# replace function helps to replace characters

'hello'.replace("l", "p")
# This will replace "l" with "p"

# tuple 
# tuple and lists are similar in nature but tuple is immutable
# tuple is defined by using () and list is defined by using []

n1=(44,55,66,77,88,99)
# slicing a tuple
n1[0:3]
# tuple is immutable, so we cannot change the value of a tuple

#tuple stores data which we do not want to change
# list stores data which we want to change

n1.index(55)
# index function gives the index of the element in the tuple
n1.count(55)    
# count function gives the number of times the element is present in the tuple

#set data function type

#set is built using {} and it is unordered and unindexed
b1={55,66,66,66,66,77,88 }

#set do not allow duplicate values
print(b1)
# set is used to store unique values
#set will remove repeated values and give unique values

#pop function in set
b1.pop()

b2=b1.copy()

b2.add(89)
b2.remove(55)
# add function in set
# remove function in set    

print(b2)

#string is built using ''
# string is immutable
#list is built using []
# list is mutable
#tupil is built using ()
# dictionary is built using {}
#set is built using {}
# dictionary is mutable but unordered and set is mutable but unordered and unindexed
# dictionary is used to store key value pairs
# set is used to store unique values

#string has following functions: replace & index
#list has following functions: append, extend, insert, remove, pop, index, count, sort, insert
#dictionary has following functions: keys, values, items, get, pop, update
#tupil has following functions: index, count
# set has following functions: add, remove, pop, copy, clear

t1=(44,55,66,77,88,99)
t1.split(',')

# split function is used to split the string into a list
# split function is not available in tuple, it is available in string

print(t1)

t2=['tsla', 'amzn', 'googl']
print(t2)

t2.join(',')
# join function is used to join the list into a string
print(t2)
# join function is not available in tuple, it is available in list

