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
 print('k') 

#type 3 loop - Use a range function to excess elements of a list
l6 = [55,66,77,88,99,100]
for i in range(len(l6)):
    print(l6[i]) #This will print each element of the list l6


#Practice Exercise 1
l7 = [4,2,6,7,55,45,67]
# WE need to find the largest number in the list l7
largest = l7[0]  # Assume the first element is the largest
for i in l7:
    if i > largest:  # If the current element is larger than the largest found so far
        largest = i  # Update the largest number
print('Largest number in the list is', largest)

# To find the smallest number in the list l7
smallest = l7[0]  # Assume the first element is the smallest
for i in l7:
    if i < smallest:  # If the current element is smaller than the smallest found so far
        smallest = i  # Update the smallest number
print('Smallest number in the list is', smallest)


#Practice Exercise 2
# We have price and volume, we need to calculate VWAP 
# FOrmula = [ (price * volume) / total volume ]

price = [100,105,110]
volume = [200,150,300]

num=0 #Have a starting point for numerator
den=0 # Hav e starting point for denominator

for k in range(len(price)):
    price_volume = price[k] * volume[k]  # Calculate price * volume for each index
    num= num + price_volume  # Sum up the numerator
    den = den + volume[k]  # Sum up the total volume
vwap = num / den  # Calculate VWAP
print('VWAP is', vwap)



