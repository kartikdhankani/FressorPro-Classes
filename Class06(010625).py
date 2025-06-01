# Class date = 01.06.2025
# Class time = 16:00 - 18:00
# Class Number = 06

# loops in python

#Anything that can use loops is called as iterable

l1=[44,55,66,77,88,99,100]

#type 1 loop

for i in l1:
    print(i)

#Above code will print each element of the list l1

#Alternatively,
print(45 in l1)  # This will return True or False

#Alternatively,
prices = [2.5,3.5,4.5]
for price in prices:
    print(price)

l2=[10,10,10,10,10,10]
total = 0
for i in l2:
    total = total + i
print(total)

#Calculating average
total = 0
prices=[2.5,3.5,4.5]

for price in prices:
    print('Price is', price)
    total = total + price
    print('Total is', total)
    average = total / len(prices)
print('Average is', average)

#Own example for summationa nd averages

stk_prices = [100, 200, 300, 400, 500]
total = 0
for price in stk_prices:
    total = total + price
average = total / len(stk_prices)
print('Total stock price is', total)    
print('Average stock price is', average)

#len #len() function returns the number of elements in a list
#len() function can be used to find the length of any iterable


#type 2 loop - Use to run a code n number of times
# print hello 100 times
#use range function to generate a sequence of numbers
list(range(100))

for i in range(100):
    print('Hello', i)

#we have to generate a list of 50 even numbers
l5=[]
for k in range(100) :  # range(100) generates numbers from 0 to 99
    if k%2 == 0: # Check if the number is even
    l5.append(k) # Append the even number to the list
 print(k) 

#type 3 loop - Use a range function to excess elements of a list
l6 = [55,66,77,88,99,100]
for i in range(len(l6)):
    print(l6[i]) #This will print each element of the list l6


