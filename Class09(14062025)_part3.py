#Class 09
#Date = 14th June 2025

#Global variable is a variable made outside a function.
#Local variable is made within a function 

def operation(num1,num2):
    print(num1,num2)
    print(num1+num2)
    print(num1/num2)

operation(4,3)
#positional argument - position of the arguments 4 & 2 is important for num1/num2
#Alternatively,

operation(num2=5,num1=10)
#Specifying num1 and num2 means it's a keyword argument.

def modify_list(list):
    list.append(4)

modify_list(list=[1,2,3])
print(list)
