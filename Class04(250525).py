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

#Now we will start with dictionaries : a new data structure in Python
#Use curly bracket to create a dictionary 

stocks_dict = {'HDFC' : 'BANK', 'TCS' : 'TECH', 'INFY' : 'TECHNOLOGY', 'RELIANCE' : 'ENERGY'}
# You can access the value using the key
print(stocks_dict['HDFC'])  # Output: 'BANK'

#The format is 'key':'value'
# value can be text or number or list or dictionary

#You can access the value using the key
print(stocks_dict['TCS'])  # Output: 'TECH'

#You can access key using the value
for key, value in stocks_dict.items():
    if value == 'TECH':
        print(key)  # Output: 'TCS' (the key for the value 'TECH')

#Alternatively we can use 'get' function to access the value using the key
print(stocks_dict.get('ReLIANCE'))  # Output: 'ENERGY'
# If the key does not exist, it will return None

print(stocks_dict.get('RELIANCE'))

#update function is used to update the value of an existing key or add a new key-value pair
stocks_dict.update({'HDFC': 'BANKING', 'WIPRO': 'TECHNOLOGY', 'NIFTY': 'INDICES'})
# This will update the value of 'HDFC' to 'BANKING' and add 'WIPRO' and 'NIFTY'

print(stocks_dict)
# You can also add a new key-value pair

#you can not have duplicate keys in a dictionary
# If you try to add a key that already exists, it will update the value
You can have duplicate values, but not duplicate keys
# For example, if you add 'HDFC' again, it will update the value

# Use type fuction to check the type of the variable
print(type(stocks_dict))  # Output: <class 'dict'>

# type function will give output as dict, int, str, list, tuple, set, etc.

stock_dict1=stocks_dict.copy()  # This will create a copy of the dictionary
print(stock_dict1)  # Output: {'HDFC': 'BANKING', 'TCS': 'TECH', 'INFY': 'TECHNOLOGY', 'RELIANCE': 'ENERGY', 'WIPRO': 'TECHNOLOGY', 'NIFTY': 'INDICES'}

stock_dict1.popitem('HDFC')  # This will remove the key-value pair with key 'HDFC'
print(stock_dict1)  # Output: {'TCS': 'TECH', 'INFY': 'TECHNOLOGY', 'RELIANCE': 'ENERGY', 'WIPRO': 'TECHNOLOGY', 'NIFTY': 'INDICES'}

# dictionary doesn't have an index, so you can't access elements by index

#There are two ways to get values from a dictionary: square brackets or get function
# Using square brackets
print(stocks_dict['TCS'])  # Output: 'TECH'
# Using get function    
print(stocks_dict.get('TCS'))  # Output: 'TECH'

#Two ways to update a dictionary: update function or square brackets
# Using update function
stocks_dict.update({'TCS': 'TECHNOLOGY'})  # This will update the value of 'TCS' to 'TECHNOLOGY'
print(stocks_dict['TCS'])  # Output: 'TECHNOLOGY'        
# Using square brackets
stocks_dict['TCS'] = 'TECHNOLOGY'  # This will also update the value of 'TCS' to 'TECHNOLOGY'
print(stocks_dict['TCS'])  # Output: 'TECHNOLOGY'

stock_dict2=stock_dict1.copy()  # This will create a copy of the dictionary
print(stock_dict2)  # Output: {'TCS': 'TECH', 'INFY': 'TECHNOLOGY', 'RELIANCE': 'ENERGY', 'WIPRO': 'TECHNOLOGY', 'NIFTY': 'INDICES'}

# To delete a key-value pair from a dictionary, you can use the del function or pop function
# Using del function
del stock_dict2['TCS']  # This will delete the key-value pair with key 'TCS'        
print(stock_dict2)  # Output: {'INFY': 'TECHNOLOGY', 'RELIANCE': 'ENERGY', 'WIPRO': 'TECHNOLOGY', 'NIFTY': 'INDICES'}
# Using pop function    
removed_value = stock_dict2.pop('INFY')  # This will remove the key-value pair with key 'INFY' and return the value
print(removed_value)  # Output: 'TECHNOLOGY'
print(stock_dict2)  # Output: {'RELIANCE': 'ENERGY', 'WIPRO': 'TECHNOLOGY', 'NIFTY': 'INDICES'}

stock_dict3= stock_dict2.copy()  # This will create a copy of the dictionary
print(stock_dict3)  # Output: {'RELIANCE': 'ENERGY', 'WIPRO': 'TECHNOLOGY', 'NIFTY': 'INDICES'} 

stock_dict3.update({'TCS': 'TECH', 'INFY': 'TECHNOLOGY', 'HCLTECH': 'TECHNOLOGY', 'ITC': 'FMCG'})  # This will add 'TCS' and 'INFY' to the dictionary

print(stock_dict3)  # Output: {'RELIANCE': 'ENERGY', 'WIPRO': 'TECHNOLOGY', 'NIFTY': 'INDICES', 'TCS': 'TECH', 'INFY': 'TECHNOLOGY', 'HCLTECH': 'TECHNOLOGY', 'ITC': 'FMCG'}

#Strings are immutable, meaning you cannot change them in place
#You need to create a new string with the updated value/string
#List and dictionaries are mutable, meaning you can change them in place

#Let's do joint function and split function in strings 

# Use [] to access elements from strings, lists and dictionaries

#split function will convert your string into a list of strings

a='hello-world'
print(a.split('-'))  # Output: ['hello', 'world']

b='a b c d e f g h i j k l m n o p q r s t u v w x y z'
c=b.split(' ')  # This will split the string into a list of strings
print(c)  # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

d=['tsla', 'aapl', 'amzn', 'googl', 'msft']
#join function will convert your list of strings into a single string   
print(', '.join(d))  # Output: 'tsla, aapl, amzn, googl, msft'
e=', '.join(d)  # This will create a new string with the elements of the list joined by ', '
print(e)  # Output: 'tsla, aapl, amzn, googl, msft'

# ALternatively, you can use a different separator
f='-'.join(d)  # This will create a new string with the elements of the list joined by '-'  
print(f)  # Output: 'tsla-aapl-amzn-googl-msft'

# Class ends here. Do not make any chages here now. Next class will be updated in Class05(290525).py

