

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


"""
# Write a Python program to convert a list of temperatures in Celsius to Fahrenheit and vice versa, outputting both results side-by-side.

"""

celsius_list = [0, 10, 20, 34.5]
fahrenheit_list = [32, 50, 68, 94.1]

for c,f in zip(celsius_list,fahrenheit_list):
    print(f"{c}°C is {f}°F")




"""
# Write a Python program that accepts a temperature string (e.g., "60C" or "45F") and converts it to the opposite scale.

"""

temp = input("Enter temperature: ")

if(temp[-1]=='C'):
    fahrenheit = (int(temp[:-1])*9/5)+32
    print(f"{temp[:-1]}°C is {fahrenheit}°F")
elif(temp[-1]=='F'):
    celsius = (int(temp[:-1])-32)*5/9
    print(f"{temp[:-1]}°F is {celsius}°C")



"""
# Write a Python program to implement temperature conversion using lambda functions and map() for a list of mixed temperature values.
"""

temps = [('C', 0), ('F', 32), ('C', 25), ('F', 77), ('C', 100)]

convert = lambda t: (
    t[0], t[1],
    'F', (t[1] * 9/5 + 32)
) if t[0] == 'C' else (
    t[0], t[1],
    'C', ((t[1] - 32) * 5/9)
)

results = list(map(convert, temps))

print("Original → Converted")
for r in results:
    print(f"{r[0]} {r[1]:6.2f} → {r[2]} {r[3]:6.2f}")

"""
# Write a Python program to validate user input for temperature conversion and re-prompt if the input format is invalid.
"""

def convert_temperature(temp_type, value):
    if temp_type == 'C':
        return (value * 9/5) + 32, 'F'
    else:
        return (value - 32) * 5/9, 'C'


while True:
    user_input = input("Enter temperature (C 25 or F 77): ").strip()

    parts = user_input.split()

 
    if len(parts) != 2:
        print("❌ Invalid format. Try again.")
        continue

    temp_type, value = parts[0].upper(), parts[1]

    if temp_type not in ['C', 'F']:
        print("❌ Temperature type must be C or F.")
        continue

    try:
        value = float(value)
    except ValueError:
        print("❌ Temperature value must be a number.")
        continue

   
    result, new_type = convert_temperature(temp_type, value)
    print(f"✅ {temp_type} {value} = {new_type} {result:.2f}")
    break
