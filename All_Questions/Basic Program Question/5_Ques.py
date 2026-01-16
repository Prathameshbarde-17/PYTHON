"""
Python Program for Compound Interest

Let us discuss the formula for compound interest. 
The formula to calculate compound interest annually is given by: 

A = P(1 + R/100) t 
Compound Interest = A - P 

Where, 

A: amount 
P: principal amount 
R: rate 
T: time span
"""

# Using Exponentiation Operator

P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest per annum: "))
T = float(input("Enter the time period in years: "))

A = P *(1 + R/100)**T
ci=A-P
print("Compound Interest is:",ci)

# Using Builtin pow() function

p=10000
r=5
t=3

A = p * pow((1 + r / 100), t)
ci=A - p
print("Compound Interest is:",ci)

# Using For Loop

p=1200
r=5.4
t=2

Amt = P
for i in range(t):
    Amt = Amt * (1+r/100)
ci = Amt - P
print("Compound Interest is:",ci)