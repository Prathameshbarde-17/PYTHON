
"""
#
2. Temperature Converter

Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

Expected Output :

60°C is 140 in Fahrenheit
45°F is 7 in Celsius

"""
temp = int(input("Enter temperature: "))

fahrenheit = (temp * 9/5)+32

celsius = (temp-32)*5/9

print(f"{temp}°F is {celsius} in Celsius\n{temp}°C is ")
print(f"{fahrenheit} in Fahrenheit")

