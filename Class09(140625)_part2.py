# Class 09
# Date - 14-06-2025
# Time - 4:30 PM 
# Topic - Function in Flight

# Functions have 3 aspects - Name of the function, Input fo rthe functions and output of the functions 

#Every function starts with a def.
#Functions need parameters like average

def average(numbers): #End a functions with colon :
    """
    This function will return average of list of numbers #This line(dock fundtion) is written for the person running the code.
    """

    total=0
    for i in numbers:
        total=total+i
    avg=total/len(numbers)

    return avg
    
prices = [1,33,44,55,66]
avg=average(prices)
print(avg)

#Note - Carefully use indentations (spaces) in function and loops

def get_fib(numbers:list)->int:

    list1=[1,1]
    num1=list1[0]
    num2=list1[1]
    for i in range(numbers-2):
        num3=num1+num2
        list1.append(num3)
        num1=num2
        num2=num3

    return list1

l=get_fib(10) #Mention number of fib numbers you need
print(l)


def add_value(num1,num2):
    return num1+num2

a=add_value(10,20)
print(a)

def print_hello():
    for i in range(5):
        print('hello')

print_hello()


#Write a function to reverse a list and reverse string

def Rev_list(list1:list)->list:
    
    end=-(len(list1)+1)
    l=range(-1,end,-1)
    print(list(l))
    ans=[]
    for i in l:
        ans.append(list1[i])
    return ans

a=Rev_list([11,22,33])
print(a)


def rev_string(word:str)->str:

    end=-(len(word)+1)
    l=range(-1,end,-1)
    print(list(l))
    ans=""
    for i in l:
        ans=ans+word[i]
    return ans

a=rev_string('sunil')
print(a)


