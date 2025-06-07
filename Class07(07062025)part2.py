#CLass 07 Part 2
#date - 07/06/2025
#day - Saturday 


list1=[44,55,63,45,23,67,56]
high=list1[0]
i=0
while True:
    if i==len(list1):
        break
    current=list1[i]
    print(current)
    if high<current:
        high=current
    i=i+1
print(high)



#Class Exercise 01 

#Get first 10 fib numbers 
#fib=1,1,2,3,5,8,13,21,34,55
#Code should take input value = 10,15 or else.

number=10
fib=[1,1]
n1=fib[0]
n2=fib[1]
for i in range (number-2):
    n3=n1+n2
    fib.append(n3)
    n1=n2
    n2=n3
print(fib)

#Using while loop
number=10
count=0
fib=[1,1]
while True:
    if count==number-2:
        break
fib.append(n3)
n1=n2
n2=n3
count=count+1
print(fib)





#Class Exercise 02
# l1 = [44,55,66,77]
# Task - We have to invert the list 

# Solution 1 using while loop

l1=[44,55,66,77]



