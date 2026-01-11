"""
 Month Name to Number of Days

Write a Python program to convert a month name to a number of days.

Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December                                
Input the name of Month: February                                       
No. of days: 28/29 days 


"""

month = input("List of months: January, February, March, April, May, June, July, August, September, October, November, December\nInput the name of Month: ")

if month =="February":
    print("No. of days: 28/29 days")
elif month == "April" or month == "June" or month == "September" or month == "November":
    print("No. of days: 30 days")
elif month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    print("No. of days: 31 days")
else:
    print("Wrong Month Name...")
