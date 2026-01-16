"""
# Python Program for Simple Interest

The task of calculating Simple Interest in Python involves taking inputs for principal amount, 
time period in years, and rate of interest per annum, applying the Simple Interest formula and 
displaying the result. 
For example, 
if p = 1000, t = 2 (years), and r = 5%, the Simple Interest is calculated using the formula and resulting in Simple Interest = 100.0.

Simple interest formula :
P is the Principal amount
T is the Time period (in years)
R is the Rate of interest per annum

 Simple Interest = (P x T x R)/100
"""

# Using function

def simple_interest(p,t,r):
    si = (p*t*r)/100
    return si
principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time period in years: "))
rate = float(input("Enter the rate of interest per annum: "))
print("simple interest is:",simple_interest(principal,time,rate))


#Using lambda function

si=lambda p,t,r:(p*t*r)/100
principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time period in years: "))
rate = float(input("Enter the rate of interest per annum: "))
print("simple interest is:",si(principal,time,rate))

#Using list comprehension

principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time period in years: "))
rate = float(input("Enter the rate of interest per annum: "))
si=[(principal*time*rate)/100]
print("simple interest is:",si)


