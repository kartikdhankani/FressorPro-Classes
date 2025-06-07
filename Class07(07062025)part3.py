#Class 07 Part 3
#Date - 07/06/2025
#Day - Saturday 


#Class Exercise 02
# l1 = [44,55,66,77]
# Task - We have to invert the list 

# Solution 1 using while loop

l1=[44,55,66,77,88]
i=-1
l2=[]
while True:
    if i==-(len(l1)+1):
        break
    current=l1[i]
    l2.append(current)
    i=i-1
print(l2)


#Solution 2 - Using for loop

print(list(range(-1,-6,-1)))


l1=[44,55,66,77,88]
l2=[]
end=-(len(l1)+1)
for i in range(-1,end,-1):
    if i==-(len(l1)+1):
        break
    current=l1[i]
    l2.append(current)
    i=i-1
print(l2)



#Class ends here 
#NExt class = Class 08
#Date = 08/06/2025
#Day = Sunday