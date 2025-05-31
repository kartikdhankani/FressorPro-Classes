#Class Date = 31.05.2025
# Class Day = Saturday
# CLass Time = 4:30 PM to 6:30 PM

# replace function helps to replace characters

'hello'.replace("l", "p")
# This will replace "l" with "p"

# tuple 
# tuple and lists are similar in nature but tuple is immutable
# tuple is defined by using () and list is defined by using []

n1=(44,55,66,77,88,99)
# slicing a tuple
n1[0:3]
# tuple is immutable, so we cannot change the value of a tuple

#tuple stores data which we do not want to change
# list stores data which we want to change

n1.index(55)
# index function gives the index of the element in the tuple
n1.count(55)    
# count function gives the number of times the element is present in the tuple

#set data function type

#set is built using {} and it is unordered and unindexed
b1={55,66,66,66,66,77,88 }

#set do not allow duplicate values
print(b1)
# set is used to store unique values
#set will remove repeated values and give unique values

#pop function in set
b1.pop()

b2=b1.copy()

b2.add(89)
b2.remove(55)
# add function in set
# remove function in set    

print(b2)

#string is built using ''
# string is immutable
#list is built using []
# list is mutable
#tupil is built using ()
# dictionary is built using {}
#set is built using {}
# dictionary is mutable but unordered and set is mutable but unordered and unindexed
# dictionary is used to store key value pairs
# set is used to store unique values

#string has following functions: replace & index
#list has following functions: append, extend, insert, remove, pop, index, count, sort, insert
#dictionary has following functions: keys, values, items, get, pop, update
#tupil has following functions: index, count
# set has following functions: add, remove, pop, copy, clear

t1=(44,55,66,77,88,99)
t1.split(',')

# split function is used to split the string into a list
# split function is not available in tuple, it is available in string

print(t1)

t2=['tsla', 'amzn', 'googl']
print(t2)

t2.join(',')
# join function is used to join the list into a string
print(t2)
# join function is not available in tuple, it is available in list

y1={'tsla':77, 'amzn':88, 'googl':99}
y1.get('tsla')
# get function is used to get the value of the key in the dictionary

#() brackets are used for call function

# Merge list within a list

l1=[[1,2,3],[4,5,6],[7,8,9]]
l1[0]
# Accessing elements in a nested list
l1[1]
# Accessing elements in a nested list

#multi-dimensional list are lists within a list

l1[1][2]
# Accessing elements in a nested list - List 2 and Element 3

l1[2][0]
# Accessing elements in a nested list - List 3 and Element 1

l2=[44,55,66,[67,57,46,[78,90,92,[12,13,14]]]]
# Now try to get 13 from this list
l2[3][3][3][1]

# dictionary of lists

d1={'tech':[333,444,555,666],'fin':[66,77,88],'gas':[89,67,45]}
# Accessing elements in a dictionary of lists
d1.get('tech')
# Accessing elements in a dictionary of lists
d1.get('tech')[2]
# Accessing elements in a dictionary of lists - List 'tech' and Element 3

d2={'tech':{'tcs':300,'amzn':780,'goog':890},'fin':{'jpmporgan':678,'hdfc':683}, 'telecom':{'jio':456, 'airtel':567}}
# Accessing elements in a dictionary of dictionaries
d2.get('tech')
d2.get('tech').get('tcs')
# Accessing elements in a dictionary of dictionaries - Dictionary 'tech' and Key 'tcs'


# Practice Exercise

hedge_fund_portfolio = {
    "fund_name": "Alpha Investments",
    "portfolio_value": 50000000,
    "investments": [
        {
            "type": "Equity",
            "holdings": [
                {"ticker": "AAPL", "quantity": 10000, "average_buy_price": 120},
                {"ticker": "TSLA", "quantity": 5000, "average_buy_price": 600}
            ]
        },
        {
            "type": "Fixed Income",
            "holdings": [
                {"bond_issue": "US Treasuries", "amount": 10000000, "yield": 1.5}
            ]
        },
        {
            "type": "Derivatives",
            "holdings": [
                {"instrument": "Options", "details": {"underlying": "GOOGL", "type": "Call", "strike_price": 1500}}
            ]
        }
    ],
    "performance_metrics": {
        "year_to_date_return": 5.2,
        "five_year_annualized_return": 7.1
    }
}

# Q1 Display the quantity of "TSLA" equity held in the portfolio.
hedge_fund_portfolio['investments'][0]['holdings'][1]['quantity']

# Q2 Add a new investment type "Real Estate" with one holding of a property "Downtown Complex" valued at 2000000.
hedge_fund_portfolio['investments'].append({"type": "Real Estate", "holdings": [{"property": "Downtown Complex", "value": 2000000}]})
print(hedge_fund_portfolio['investments'])

#Q3 Update the portfolio value to 51000000.
hedge_fund_portfolio['portfolio_value'] = 51000000
print(hedge_fund_portfolio['portfolio_value'])



#Practice Exercise 2

credit_risk_profiles = {
    "individuals": [
        {
            "name": "John Doe",
            "credit_score": 750,
            "outstanding_loans": {
                "auto_loan": {"amount": 20000, "interest_rate": 3.5},
                "home_loan": {"amount": 150000, "interest_rate": 2.8}
            },
            "payment_history": [("2024-01-10", "On Time"), ("2024-01-01", "Late")]
        },
        {
            "name": "Jane Smith",
            "credit_score": 680,
            "outstanding_loans": {
                "credit_card": {"amount": 5000, "interest_rate": 12.0}
            },
            "payment_history": [("2024-01-10", "On Time")]
        }
    ]
}

# get the value 12.0 from the credit_risk_profiles dictionary
a=credit_risk_profiles['individuals'][1]['outstanding_loans']['credit_card']['interest_rate']
print(a)
#individua's is a list and we are accessing the second element in the list using index 1
b=credit_risk_profiles['individuals'][1]
print(b)
# now you will get a dictionary as output, use 'outsstanding_loans' to get the value of the key 'credit_card'

# Q2 Get "Late" string from the payment history of John Doe.

a1=credit_risk_profiles
print(a1)
#a1 will give a dictionary 

a2=credit_risk_profiles.get['individuals'][0]
print(a2)


#practice Exercise 3

foreign_exchange = {
    "base_currency": "USD",
    "exchange_rates": {
        "EUR": {
            "current_rate": 0.85,
            "historical_rates": [
                {"date": "2024-01-10", "rate": 0.84},
                {"date": "2024-01-09", "rate": 0.85}
            ]
        },
        "JPY": {
            "current_rate": 110.00,
            "historical_rates": [
                {"date": "2024-01-10", "rate": 109.50},
                {"date": "2024-01-09", "rate": 110.20}
            ]
        }
    }
}

# Task: Get "110.00" from the foreign_exchange dictionary.
a3=foreign_exchange.get('exchange_rates').get('JPY').get('current_rate')
print(a3)

#Task: Get "2024-01-09" from the historical rates of EUR.
foreign_exchange.get('exchange_rates').get('EUR').get('historical_rates')[1].get('date')
# This will give you the date "2024-01-09" from the historical rates of EUR




#Practice exercise

investment_portfolio = {
    "investor_name": "Jane Doe",
    "portfolio_id": "JD1234",
    "assets": {
        "stocks": [
            {
                "ticker": "AAPL",
                "quantity": 50,
                "purchase_price": 120.00,
                "current_price": 130.00
            },
            {
                "ticker": "MSFT",
                "quantity": 30,
                "purchase_price": 200.00,
                "current_price": 210.00
            }
        ],
        "bonds": [
            {
                "identifier": "US123456",
                "quantity": 100,
                "purchase_price": 1000.00,
                "current_price": 1020.00,
                "maturity_date": "2030-01-01"
            }
        ],
        "mutual_funds": [
            {
                "name": "XYZ Growth Fund",
                "quantity": 200,
                "purchase_price": 15.00,
                "current_price": 15.50
            }
        ]
    },
    "cash_holdings": 10000.00,
    "investment_goals": {"retirement": 2035, "education": 2025}
}


#Task: get value of "210"
investment_portfolio['assets']['stocks'][1]['current_price']

#alternative way to get the value of "210"; use get function
investment_portfolio.get('assets').get('stocks')[1].get('current_price')


# New data structure: None data Type

N=None
print(N)
print(type(N))
# None is a special data type in Python that represents the absence of a value or a null value.
type(N)

#Truthy value and Fasly value
#EVerything is a truthy value unless they are falsy value 
#All strings are truthy value unless they are empty string
#All empty strings, empty lists, empty tuples, empty dictionaries, and None are falsy values
#Truthy values are values that evaluate to True in a boolean context

#Example - 

m=11
n=12

if abs:
    print(True)
else:
    print(False)

# Alternatively,

if 0: 
    print(True)
else: 
    print(False) 

# This will print False because 0 is a falsy value

if None: 
    print(True)
else: 
    print(False) 
# This will print False because None is a falsy value

# Next class in class06(010625).py
# The class ends here. Please continue to the next class for more advanced topics.