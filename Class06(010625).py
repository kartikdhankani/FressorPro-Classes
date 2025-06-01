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

#pratcice Exercise 3
#Calculate total dividend from a list of dividends and quantity of shares
div=[0.5,1,0.2]
stk_qty=[100,200,150]
total_dividend = 0  # Initialize total dividend to 0
for j in range(len(div)):
    total_dividend += div[j] * stk_qty[j]  # Calculate dividend for each stock and add to total
print('Total dividend is', total_dividend)

#practice Exercise 4
#Calculate number of profitable trades from a PNL list
pnl = [20,-10,15,-5,30]

profitable_trades = 0  # Initialize counter for profitable trades

for i in pnl:
    if i>0 :
        profitable_trades = profitable_trades + 1 # += 1 will increment the counter by 1 for each profitable trade 
print('Number of profitable trades:', profitable_trades)

# Type 4 loop - Go through dictionary 

d1 = {'tcs':600, 'amzn':700, 'googl':890}

for i in d1: 
    print(i, d1[i])  # This will print each key and its corresponding value in the dictionary d1

print(list(d1.keys()))  # This will print all the keys in the dictionary d1
print(list(d1.values()))  # This will print all the values in the dictionary d1
print(list(d1.items()))  # This will print all the key-value pairs in the dictionary d1

for i in d1.keys():
    print(i, d1[i])  # This will print each key and its corresponding value in the dictionary d1

for j in d1.values():
    print(j)  # This will print each value in the dictionary d1

for k,l in d1.items():
    print(k, l)  # This will print each key and its corresponding value in the dictionary d1


i=0
while True:
    if i==20:  # Break the loop when i reaches 20
        break
    print(i)
    i = i+1



#practice Exercise 5
#Get all the even numbers between 1 and 100

even_numbers = []  # Initialize an empty list to store even numbers
for i in range(1, 101):  # Loop through numbers from 1 to 100
    if i % 2 == 0:  # Check if the number is even
        even_numbers.append(i)  # Add the even number to the list   
print('Even numbers between 1 and 100:', even_numbers)  # Print the list of even numbers

# Practice Exercise 6

#Get a multiplication table for a given number
num1=3
num2=0
while True:
    if num2 ==101:
        break
    print(num1,'X',num2, '=', num1*num2)  # Print the multiplication table for num1
    num2 += 1  # Increment num2 by 1 in each iteration


    #Class ends here
    #Next class will be on 08.06.2025
#Class time = 16:00 - 18:00
#Class Number = 07

