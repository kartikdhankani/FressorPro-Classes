#Class 10
#Date - 15th June 2025

#Practise Exercise 01

#reversing a string 

def rev_string(word:str)->str:
    l=len(word)
    indexes=range(-1,-(l+1),-1)
    ans=""
    for i in indexes:
        ans=ans+word[i]
        return ans
    
def rev_string2(word:str)->str:
    ans=''
    for i in word:
        ans=i+ans
    return ans

def is_plaindrome(word:str)->bool:
    rev_word=rev_string(word)
    print(rev_word)
    if word==rev_word:
        return True
    else:
        return False
    
word='level'
a=is_plaindrome(word)
print(a)
print(rev_string2('tsla'))



#Practise Exercise 02 = Merge two lists

l1 = [33,44,55]
l2=[66,77,88]
print(l1+l2)

#Alternatively,

for i in l2:
    l1.append(i)
print(l1)


# Practice exercise 03 = WHn the investment will become double?

#Simple Interest
Capital=1000
interest=10
years=0
current_money=Capital
while True:
    if current_money>2*Capital:
        break
    perc_interest=Capital*(interest/100)
    current_money=current_money+perc_interest
    years=years+1

print(years)

#Compounding Interest

def get_year(capital:int, interest:int):
    pass

#Complete this afterwards




#Practice Exercise 04 - Number of shares after reinvestment

def get_share(qty,div,price,years):

    total_value=qty*price

    for i in range(years):
        total_value=total_value+(div*qty)
        qty=total_value/price
    final=total_value/price
    return final

f=get_share(100,2,50,5)
print(f)


#Practice Exercise 05

def pen_fund(initial,monthly,int,dur):

    current=initial 
    for i in range(1,(dur*12)+1):
        if i%12==0:
            current_int=(current+(interest/12))
            current=current+monthly+current_int
            current_int
            print(i,current_int)
        else:
            print(i)
            current=current+monthly
    return current

c=pen_fund(50000,200,0.06,20)
print(c)



#Practice exercise 06
#Moving average calculator

closing_prices=list(range(101,150))
print(closing_prices)
mv=5

sma=[]
for i in range(len(closing_prices)):
    if i<mv:
        sma.append(closing_prices[i])
    else:
        last_mv=closing_prices[i-5:i]
        avg=sum(last_mv)/mv
        sma.append(avg)
print(sma)




