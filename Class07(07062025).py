#class 07
#day = Saturday
#date = 07/06/2025 



#stk_prices={'tsla':700, 'goog':900,'amzn':68, 'nvda':567}
#portfolio=[]
#while True:
#    name=input('enter the stock name (q to Quit)')
#    if name.upper()=='Q':
#        break
#    found=stk_prices.get(name)
#   if found:
#        portfolio.append(name)
#    else:
#        print('this stock name is invalid, type again')
#    portfolio.append(name)

#print(portfolio)


#break function will break the loop.

#continue function will continue the loop.

#stk_prices={'tsla':700, 'goog':900,'amzn':68, 'nvda':567}
#portfolio=[]
#while True:
#    name=input('enter the stock name (q to Quit)')
#    if name.upper()=='Q':
#        break
#    if name=='nvda':
#        print('you cannot trade this stock try something else')
#        continue

#    found=stk_prices.get(name)
#    if found:
#        portfolio.append(name)
#    else:
#        print('this stock name is invalid type again')
#    print(portfolio)


list1=[44,55,63,45,23,67,56]
high=list1[0]
i=0
while True:
    if i==len(list1):
        break
    print(list[i])
if high<list1[i]:
    high=list1[i]
    i=i+1
print(high)